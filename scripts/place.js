function calculateWindChill(tempF, speedMph) {
  return (
    35.74 +
    0.6215 * tempF -
    35.75 * Math.pow(speedMph, 0.16) +
    0.4275 * tempF * Math.pow(speedMph, 0.16)
  ).toFixed(2);
}

// Footer info
document.getElementById("year").textContent = new Date().getFullYear();
document.getElementById("lastModified").textContent = document.lastModified;

// Windchill logic
const temp = parseFloat(document.getElementById("temperature").textContent);
const wind = parseFloat(document.getElementById("windSpeed").textContent);
const output = document.getElementById("windChill");

if (temp <= 50 && wind > 3) {
  output.textContent = `${calculateWindChill(temp, wind)} °F`;
} else {
  output.textContent = "N/A";
}
