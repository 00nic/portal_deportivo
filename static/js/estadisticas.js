document.addEventListener('DOMContentLoaded', function () {
    const equiposLabels = JSON.parse(document.getElementById('equiposLabels').textContent);
    const partidosJugadosValues = JSON.parse(document.getElementById('partidosJugadosValues').textContent);
    const partidosGanadosValues = JSON.parse(document.getElementById('partidosGanadosValues').textContent);
    const partidosPerdidosValues = JSON.parse(document.getElementById('partidosPerdidosValues').textContent);
    const partidosEmpatadosValues = JSON.parse(document.getElementById('partidosEmpatadosValues').textContent);
    const jugadoresLabels = JSON.parse(document.getElementById('jugadoresLabels').textContent);
    const golesTotalesValues = JSON.parse(document.getElementById('golesTotalesValues').textContent);
    const asistenciasTotalesValues = JSON.parse(document.getElementById('asistenciasTotalesValues').textContent);
    const partidosTotalesValues = JSON.parse(document.getElementById('partidosTotalesValues').textContent);

    
    equiposLabels.forEach((label, index) => {
        let ctx = document.getElementById(`grafico-equipo-${index + 1}`).getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Partidos Jugados', 'Partidos Ganados', 'Partidos Perdidos', 'Partidos Empatados'],
                datasets: [{
                    label: `${label}`,
                    data: [
                        partidosJugadosValues[index],
                        partidosGanadosValues[index],
                        partidosPerdidosValues[index],
                        partidosEmpatadosValues[index]
                    ],
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.2)',    
                        'rgba(199, 199, 199, 0.2)',    
                        'rgba(255, 99, 132, 0.2)',    
                        'rgba(255, 159, 64, 0.2)'     
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)',      
                        'rgba(199, 199, 199, 1)',      
                        'rgba(255, 99, 132, 1)',      
                        'rgba(255, 159, 64, 1)'       
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: `${label}`,
                        font: {
                            size: 18
                        },
                        padding: {
                            top: 10,
                            bottom: 20
                        }
                    }
                },
            }
        });
    });

    
    jugadoresLabels.forEach((label, index) => {
        let ctx = document.getElementById(`grafico-jugador-${index + 1}`).getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Goles Totales', 'Asistencias Totales', 'Partidos Totales'],
                datasets: [{
                    label: `${label}`,
                    data: [
                        golesTotalesValues[index],
                        asistenciasTotalesValues[index],
                        partidosTotalesValues[index]
                    ],
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.2)',    
                        'rgba(255, 159, 64, 0.2)',    
                        'rgba(199, 199, 199, 0.2)',    
                        'rgba(255, 99, 132, 0.2)'    
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)',      
                        'rgba(255, 159, 64, 1)',      
                        'rgba(199, 199, 199, 1)',      
                        'rgba(255, 99, 132, 1)'     
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: `${label}`,
                        font: {
                            size: 18
                        },
                        padding: {
                            top: 10,
                            bottom: 20
                        }
                    }
                }
            }
        });
    });
});
