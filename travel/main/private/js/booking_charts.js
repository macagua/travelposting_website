//Booking char config
$.getJSON("/destinations/booking-charts/", function(data){

    $('#booking-chart').highcharts({
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 45,
                beta: 0
            }
        },

        title: {
            text: ''
        },

        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },

        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                depth: 35,
                dataLabels: {
                    enabled: true,
                    format: '{point.name}'
                }
            }
        },

        series: [{
            type: 'pie',
            name: 'Porcentaje',
            data: data
        }]
    });

});


$.getJSON("/destinations/destination-charts/", function(data){
    var myChart = Highcharts.chart('destination-chart', {
        chart: {
            type: 'bar'
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: ['', '']
        },
        yAxis: {
            title: {
                text: 'all your destinations'
            }
        },

        series: [{
                    name: 'Published',
                    data: data[1]
                }, {
                    name: 'Unpublished',
                    data: data[0]
                }]
    });
});
