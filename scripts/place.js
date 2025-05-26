function calculateWindChillCelsius(tempC, speedKmH) {
  return (
    13.12 +
    0.6215 * tempC -
    11.37 * Math.pow(speedKmH, 0.16) +
    0.3965 * tempC * Math.pow(speedKmH, 0.16)
  ).toFixed(2);
}

// ----------------
document.getElementById("currentyear").textContent = new Date().getFullYear();
document.getElementById("lastModified").textContent = `Last Modification: ${document.lastModified}`;

// ----------------------
const temp = parseFloat(document.getElementById("temperature").textContent);
const wind = parseFloat(document.getElementById("windSpeed").textContent);
const output = document.getElementById("windChill");

// ---------------------------
if (temp <= 10 && wind > 4.8) {
  output.textContent = `${calculateWindChillCelsius(temp, wind)} °C`;
} else {
  output.textContent = "N/A";
}