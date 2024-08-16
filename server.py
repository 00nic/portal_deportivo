from flask import Flask, render_template
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import bcrypt

app = Flask(__name__)
load_dotenv()

app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def main():
    return render_template('datosFutbol.html')

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
