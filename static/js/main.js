function navResponsive() {
  var e = document.getElementById("idNavbar");
  if (e.className === "navbar navbar_colored") {
    e.className += " responsive";
  } else {
    e.className = "navbar navbar_colored";
  }
}

function iconEffect(x) {
  x.classList.toggle("change");
}