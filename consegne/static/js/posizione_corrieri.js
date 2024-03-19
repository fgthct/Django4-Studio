
// Inizializza la mappa Leaflet per l'elenco consegne
var mapConsegne = L.map('map-consegne').setView([37.5021, 15.0873], 13);

// Aggiungi un layer di mappa OpenStreetMap per l'elenco consegne
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mapConsegne);


// Itera sui corrieri e aggiungi i marcatori alla mappa
corrieriData.forEach(function (corriere) {
    var marker = L.marker([corriere.posizione_attuale.y, corriere.posizione_attuale.x]).addTo(mapConsegne);
    marker.bindPopup("<b>Corriere:</b> " + corriere.nome + "<br><b>Posizione:</b> " + formatCoordinates(corriere.posizione_attuale.y) + ", " + formatCoordinates(corriere.posizione_attuale.x));
});

function formatCoordinates(coordinate) {
    return coordinate.toFixed(6);
}

// Stampa il contenuto di corrieriData in console
// console.log(corrieriData);

// Aggiungi un singolo marcatore sulla mappa
// var singleMarker = L.marker([37.510761, 14.966331]).addTo(mapConsegne);
// singleMarker.bindPopup("<b>Posizione di test</b>").openPopup();

// Aggiungi un singolo marcatore sulla mappa
// var singleMarker = L.marker([37.502457, 15.087120]).addTo(mapConsegne);
// singleMarker.bindPopup("<b>Posizione poste italiane</b>").openPopup();

// Aggiungi un singolo marcatore sulla mappa
// var singleMarker = L.marker([37.510761, 14.966331]).addTo(mapConsegne);
// singleMarker.bindPopup("<b>Posizione Pero Sciutti</b>").openPopup();

//14.966331, 37.510761
