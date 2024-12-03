
const imagenes = [
    { id: "imagen1", link: "https://view.genially.com/5e583e037a57930fe3930592/presentation-proyecto-avengers" },
    { id: "imagen2", link: "https://elblogdemiaulasextoc.wordpress.com/2023/10/08/masterchef/" },
    { id: "imagen3", link: "https://riucv.ucv.es/bitstream/handle/20.500.12466/1984/TFG_Cynthia_Albert_%20Ferrandis.pdf" }
];

// Asignar enlaces dinámicamente a cada imagen
imagenes.forEach(function(imagen) {
    document.getElementById(imagen.id).onclick = function() {
        window.location.href = imagen.link;
    };
});

