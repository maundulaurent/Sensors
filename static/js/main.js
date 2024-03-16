// JavaScript code to initialize and update the circular gauge
// You can use libraries like D3.js for more advanced gauges

// Example function to update the gauge value
function updateGauge(gaugeId, value) {
    // Your update logic here
}


function updateGauge() {
    var gaugeValue = document.getElementById("gaugeValue").value;
    var percentage = gaugeValue + "%";
    var progressCircle = document.getElementById("progressCircle1");
    progressCircle.style.strokeDasharray = percentage + " 126"; // Adjust 126 according to your gauge size
}

// ================= //

function updateGauge() {
    var gaugeValue = document.getElementById("gaugeValue").value;
    var percentage = gaugeValue / 100;
    var progressCircle = document.getElementById("progressCircle1");

    // Calculate the length of the arc based on the percentage
    var totalLength = Math.PI * 80; // Circumference of a circle with radius 40
    var dashLength = totalLength * percentage;

    // Set the stroke-dasharray to make the blue color reach up to the desired marking
    progressCircle.style.strokeDasharray = dashLength + " " + totalLength;

    // Update pointer position
    var pointer = document.getElementById("pointer");
    var angle = gaugeValue * 1.8; // Each percentage corresponds to 1.8 degrees in a half circle
    var x = 50 + 40 * Math.cos(Math.PI * angle / 180); // Calculate x coordinate
    var y = 25 + 40 * Math.sin(Math.PI * angle / 180); // Calculate y coordinate
    pointer.setAttribute("cx", x);
    pointer.setAttribute("cy", y);
}


//
$(function () {
    function updateGauge() {
      var gaugeValue = document.getElementById("gaugeValue").value;
      var percentage = gaugeValue / 100;
      var progressCircle = document.getElementById("progressCircle1");
  
      // Calculate the length of the arc based on the percentage
      var totalLength = Math.PI * 80; // Circumference of a circle with radius 40
      var dashLength = totalLength * percentage;
  
      // Set the stroke-dasharray to make the blue color reach up to the desired marking
      progressCircle.style.strokeDasharray = dashLength + " " + totalLength;
  
      // Update pointer position
      var pointer = document.getElementById("pointer");
      var angle = gaugeValue * 1.8; // Each percentage corresponds to 1.8 degrees in a half circle
      var x = 50 + 40 * Math.cos(Math.PI * angle / 180); // Calculate x coordinate
      var y = 25 + 40 * Math.sin(Math.PI * angle / 180); // Calculate y coordinate
      pointer.setAttribute("cx", x);
      pointer.setAttribute("cy", y);
    }
  
    // Call updateGauge function on input change
    $("#gaugeValue").on("input", function () {
      updateGauge();
    });
  
    // Initialize gauge with default value
    updateGauge();
  });
  