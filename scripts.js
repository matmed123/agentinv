document.addEventListener('DOMContentLoaded', function() {
    const ctx1 = document.getElementById('chart1').getContext('2d');
    const ctx2 = document.getElementById('chart2').getContext('2d');
    const ctx3 = document.getElementById('chart3').getContext('2d');
    const ctx4 = document.getElementById('chart4').getContext('2d');
    const ctx5 = document.getElementById('chart5').getContext('2d');

    const chart1 = new Chart(ctx1, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Mercado 1',
                data: [],
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }
            }
        }
    });

    // ...similar code for chart2, chart3, chart4, chart5...

    function updateChart(chart, data) {
        chart.data.labels.push(new Date());
        chart.data.datasets[0].data.push(data);
        chart.update();
    }

    setInterval(() => {
        updateChart(chart1, Math.random() * 100);
        // ...similar code for chart2, chart3, chart4, chart5...
    }, 1000);

    document.getElementById('btn1').addEventListener('click', () => {
        alert('Función 1 activada');
    });

    // ...similar code for btn2, btn3, btn4...
});
