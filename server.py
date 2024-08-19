from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import bcrypt

app = Flask(__name__)
load_dotenv()

app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = '4848'

mysql = MySQL(app)

@app.route('/')
def main():
    return redirect(url_for('login'))

@app.route('/vista_partidos')
def vista_partidos():
    return render_template("index.html")



@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        clave = request.form['clave']
        
        hashed_pass = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())

        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (nombre, apellido, correo, contraseña) VALUES (%s, %s, %s, %s)",
                        (nombre, apellido, correo, hashed_pass.decode('utf-8')))
            mysql.connection.commit()
            cur.close()
            flash('Registro exitoso. Puedes iniciar sesión ahora.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error al guardar los datos: {e}', 'danger')
            return redirect(url_for('registro'))

    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        clave = request.form['clave']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT contraseña FROM users WHERE correo = %s", (correo,))
        result = cur.fetchone()
        cur.close()

        if result and bcrypt.checkpw(clave.encode('utf-8'), result['contraseña'].encode('utf-8')):
            session['correo'] = correo
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('noti'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route("/portal")
def noti():
    return render_template("portal.html")

@app.route("/noti1")
def notic():
    return render_template("noti1.html")


@app.route('/logout')
def logout():
    session.pop('correo', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))


@app.route('/estadisticas')
def estadisticas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM equipos')
    equipos = cur.fetchall()
    jugadores = {}
    for equipo in equipos:
        seleccion = equipo['pais']
        cur.execute('SELECT * FROM jugadores WHERE seleccion = %s', (seleccion,))
        jugadores[seleccion] = cur.fetchall()
    
    equipos_labels = [equipo['equipo_nombre'] for equipo in equipos]
    partidos_jugados_values = [equipo['partidos_jugados'] for equipo in equipos]
    partidos_ganados_values = [equipo['partidos_ganados'] for equipo in equipos]
    partidos_perdidos_values = [equipo['partidos_perdidos'] for equipo in equipos]
    partidos_empatados_values = [equipo['partidos_empatados'] for equipo in equipos]

    jugadores_labels = []
    goles_totales_values = []
    asistencias_totales_values = []
    partidos_totales_values = []

    for equipo, jugadores_list in jugadores.items():
        for jugador in jugadores_list:
            jugadores_labels.append(jugador['nombre_completo'])
            goles_totales_values.append(jugador['goles_totales'])
            asistencias_totales_values.append(jugador['asistencias_totales'])
            partidos_totales_values.append(jugador['partidos_totales'])

    cur.close()

    return render_template('estadisticas.html', equipos=equipos, jugadores=jugadores, equipos_labels=equipos_labels,
                        partidos_jugados_values=partidos_jugados_values,
                        partidos_ganados_values=partidos_ganados_values,
                        partidos_perdidos_values=partidos_perdidos_values,
                        partidos_empatados_values=partidos_empatados_values,
                        jugadores_labels=jugadores_labels,
                        goles_totales_values=goles_totales_values,
                        asistencias_totales_values=asistencias_totales_values,
                        partidos_totales_values=partidos_totales_values)


@app.route('/cuartos')
def cuartos():
    return render_template('cuartoss.html')

@app.route('/semis')
def semis():
    return render_template('semis.html')

@app.route('/final')
def final():
    return render_template('final.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
