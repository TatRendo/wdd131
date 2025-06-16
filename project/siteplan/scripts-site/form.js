const products = [
  { id: "th-001", name: "Thiogamma", averagerating: 4.8 },
  { id: "an-002", name: "Ankermann", averagerating: 4.6 }
];

const select = document.getElementById("productName");
products.forEach(product => {
  const option = document.createElement("option");
  option.value = product.id;
  option.textContent = product.name;
  select.appendChild(option);
});
