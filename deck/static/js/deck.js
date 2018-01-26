var deck = [];

$( document ).ready(function() {
    console.log( "ready!" );

    $(".card").click(function () {
        deck.push(parseInt(this.id));
        $('#newdeck').empty()
        deck.forEach(function (value) {
                $('#newdeck').append("<tr><td>"+value+"</td></tr>")
        })
    });
    $("#senddeck").click(function () {
        var nom = document.getElementById("nomdeck").value;
        console.log(deck);
        var jsondeck = JSON.stringify(deck);
        var data = "{\"name\":\""+nom+"\",\"cards\":"+jsondeck+"}";
        console.log(data);

        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", "http://10.13.7.217:8000/mydeck/deck", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(JSON.stringify(data));
        var responce = JSON.parse(xhttp.responseText);
        console.log(responce);
    })

});


