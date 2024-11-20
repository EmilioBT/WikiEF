
const imagenes = [
    { id: "imagen1", link: "https://www.google.com" },
    { id: "imagen2", link: "https://www.youtube.com" },
    { id: "imagen3", link: "https://www.facebook.com" }
];

// Asignar enlaces dinámicamente a cada imagen
imagenes.forEach(function(imagen) {
    document.getElementById(imagen.id).onclick = function() {
        window.location.href = imagen.link;
    };
});

