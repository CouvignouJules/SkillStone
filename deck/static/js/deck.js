var deck = [];
var nom

$( document ).ready(function() {
    console.log( "ready!" );

    $(".card").click(function () {
        deck.push(this.id);
        $('#newdeck').empty()
        deck.forEach(function (value) {
                $('#newdeck').append("<tr><td>"+value+"</td></tr>")
        })
    });
    
});


