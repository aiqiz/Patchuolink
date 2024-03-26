'use strict';

//
// Sales chart
//

var Chart1 = (function() {

  var $chart1 = $('#chart-dark');

  function init($chart1, labels, data) {
    var chartData1 = JSON.parse('{{ c1 | safe }}');
    console.log(chartData1);
    var ctx = document.getElementById('chart-dark').getContext('2d');
    var chart1 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartData1.labels,
            datasets: [{
                label: 'Surface Temperature',
                data: chartData1.values
            }]
        }
    });
}

  
  $('#chart-dark').data('chart', chart1);
  // Events

  if ($chart1.length) {
    init($chart1);
  }

})();
