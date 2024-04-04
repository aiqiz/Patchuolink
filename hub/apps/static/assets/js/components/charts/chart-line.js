'use strict';

//
// Sales chart
//

var Chart = (function() {
  console.log("hello")
  // Variables

  var $chart = $('#chart-dark');

  function init($chart) {
    
    var output_chart = new Chart($chart, {
      type: 'line',
      options: {
        scales: {
          yAxes: [{
            gridLines: {
              lineWidth: 1,
              color: Chart.colors.gray[900],
              zeroLineColor: Chart.colors.gray[900]
            },
            ticks: {
              callback: function(value) {
                if (!(value % 10)) {
                  return '$' + value + 'k';
                }
              }
            }
          }]
        }},
      data: {
        labels: JSON.parse('{{ c1 | safe }}').labels,
        datasets: [{
          label: 'Surface Temperature',
          data: JSON.parse('{{ c1 | safe }}').values
        }]
      }
    });
    $chart.data('chart', output_chart);
  };



  if ($chart.length) {
    init($chart);
  }

})();
