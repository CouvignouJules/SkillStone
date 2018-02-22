var deck = [];

$( document ).ready(function() {
    console.log( "ready!" );

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken);

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
        var token = document.getElementById("token").innerHTML;
        console.log(token);
        var data = "{\"name\":\""+nom+"\",\"cards\":"+jsondeck+"}";
        console.log(data);

        $.ajax({
            type: "POST",
            url: "http://localhost:8000/mydeck/deck",
            dataType: "json",
            headers: {
                "Authorization": token ,
                'X-CSRFToken': csrftoken,
                "Content-Type":'application/json'
            },
            data : data,
            success: function (msg) {
                console.log('Success!',msg)
            },
            error : function(err) {
                console.log('Error!', err)
            },
       });
    })
});


