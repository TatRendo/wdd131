const temples = [
    //1
  {
    templeName: "Bogota Temple",
    location: "Bogota, Colombia",
    dedicated: "1999, April, 24",
    area: 11113,
    imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/bogota-colombia/800x500/bogota-colombia-temple-lds-1029726-wallpaper.jpg"
  },
  //2
  {
    templeName: "Los Olivos Temple",
    location: "Lima, Peru",
    dedicated: "2024, January, 14",
    area: 11111,
    imageUrl: "https://churchofjesuschristtemples.org/assets/img/temples/lima-peru-los-olivos-temple/lima-peru-los-olivos-temple-42502.jpg"
  },
  //3
  {
    templeName: "Lindon Utah Temple",
    location: "Lindon, Utah, United States",
    dedicated: "2022, April, 23",
    area: 11113,
    imageUrl: "https://churchofjesuschristtemples.org/assets/img/temples/lindon-utah-temple/lindon-utah-temple-60718.jpg"
  },
  //4
  {
    templeName: "Freiberg Temple",
    location: "Freiberg, Germany",
    dedicated: "1985, Jun, 29",
    area: 11111,
    imageUrl: "https://churchofjesuschristtemples.org/assets/img/temples/freiberg-germany-temple/freiberg-germany-temple-4062.jpg"
  },
  //4
  {
    templeName: "Barranquilla Temple",
    location: "Barranquilla, Colombia",
    dedicated: "2018, December, 9",
    area: 11111,
    imageUrl: "https://churchofjesuschristtemples.org/assets/img/temples/barranquilla-colombia-temple/barranquilla-colombia-temple-43.jpg"
  },
  //5
  {
    templeName: "London Temple",
    location: "London, England",
    dedicated: "1958, September, 7",
    area: 11110,
    imageUrl: "https://churchofjesuschristtemples.org/assets/img/temples/london-england-temple/london-england-temple-56886.jpg"
  },
  //6
  {
    templeName: "Orlando Temple",
    location: "Orlando, Florida, United States",
    dedicated: "1994, October, 9",
    area: 11110,
    imageUrl: "https://churchofjesuschristtemples.org/assets/img/temples/orlando-florida-temple/orlando-florida-temple-51569.jpg"
  },
  //7
  {
    templeName: "Madrid Temple",
    location: "Madrid, Spain",
    dedicated: "1999, March, 19",
    area: 11115,
    imageUrl: "https://churchofjesuschristtemples.org/assets/img/temples/madrid-spain-temple/madrid-spain-temple-54286.jpg"
  },
  
];

const container = document.querySelector("#temple-cards");
const filterTitle = document.querySelector("#filter-title");

// display function - nuevo
function displayTemples(list) {
  container.innerHTML = "";
  list.forEach(temple => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <h3>${temple.templeName}</h3>
      <p><strong>Location:</strong> ${temple.location}</p>
      <p><strong>Dedicated:</strong> ${temple.dedicated}</p>
      <p><strong>Size:</strong> ${temple.area.toLocaleString()} sq ft</p>
      <img src="${temple.imageUrl}" loading="lazy" alt="${temple.templeName} Temple">
    `;
    container.appendChild(card);
  });
}

// aqui cambio tamaños y antiguedad etc.
function filterTemples(criteria) {
  let filtered;
  switch (criteria) {
    case "old":
      filtered = temples.filter(t => parseInt(t.dedicated.split(",")[0]) < 1999);
      filterTitle.textContent = "Old Temples";
      break;
    case "new":
      filtered = temples.filter(t => parseInt(t.dedicated.split(",")[0]) > 2000);
      filterTitle.textContent = "New Temples";
      break;
    case "large":
      filtered = temples.filter(t => t.area > 10000);
      filterTitle.textContent = "Large Temples";
      break;
    case "small":
      filtered = temples.filter(t => t.area < 11112);
      filterTitle.textContent = "Small Temples";
      break;
    default:
      filtered = temples;
      filterTitle.textContent = "Home";
  }
  displayTemples(filtered);
}


document.querySelectorAll("nav button").forEach(button =>
  button.addEventListener("click", () => filterTemples(button.dataset.filter))
);

document.getElementById("currentyear").textContent = new Date().getFullYear();
document.getElementById("lastModified").textContent = `Last Modification: ${document.lastModified}`;

// nuevo
displayTemples(temples);