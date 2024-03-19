// static/js/main.js
$(document).ready(function () {
    // Funzione per caricare l'elenco dei corrieri e delle consegne all'avvio della pagina
    function caricaElencoCorrieri() {
        $.ajax({
            url: '/consegne/elenco_corrieri/',
            type: 'GET',
            success: function (data) {
                // Aggiungi i corrieri all'elenco
                data.forEach(function (corriere) {
                    $('#lista_corrieri').append('<li>' + corriere.nome + ' - ' + corriere.posizione_attuale + '</li>');
                });
            }
        });

        // Carica l'elenco delle consegne
        $.ajax({
            url: '/consegne/elenco_consegne/',
            type: 'GET',
            success: function (data) {
                // Aggiungi le consegne all'elenco
                data.forEach(function (consegna) {
                    $('#lista_consegne').append('<li>' + consegna.destinatario + ' - ' + consegna.indirizzo_destinazione + '</li>');
                });
            }
        });
    }

    // Chiama la funzione per caricare l'elenco dei corrieri e delle consegne all'avvio della pagina
    caricaElencoCorrieri();

    // Evento di invio del form per creare una nuova consegna
    $('#form-nuova-consegna').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: '/consegne/nuova_consegna/',
            type: 'POST',
            data: formData,
            success: function (response) {
                console.log('Consegna creata con successo');
                // Ricarica l'elenco dei corrieri e delle consegne dopo aver creato una nuova consegna
                $('#lista_corrieri').empty();
                $('#lista_consegne').empty();
                caricaElencoCorrieri();
            }
        });
    });

});
