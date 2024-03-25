'use strict';

//
// Sales chart
//

var Chart1 = (function() {

  var $chart = $('#chart-dark');

  function init($chart, labels, data) {
    var salesChart = new Chart($chart, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Performance',
          data: data
        }]
      }
    });
    $chart.data('chart', Chart1);
}


  // Events

  if ($chart.length) {
    init($chart);
  }

})();
