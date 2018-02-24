var deck = [];
var token;
var csrftoken;

$( document ).ready(function() {
    token = document.getElementById("token").innerHTML;
    csrftoken = getCookie('csrftoken');

    $(".card").click(function () {
        deck.push(parseInt(this.id));
        $('#newdeck').append("<tr><td class='newDeckCard' id="+this.id+">"+this.innerHTML+"</td></tr>")
    });

    $("#senddeck").click(function () {
        var nom = document.getElementById("nomdeck").value;
        var jsondeck = JSON.stringify(deck);
        var data = "{\"name\":\""+nom+"\",\"cards\":"+jsondeck+"}";

        $.ajax({
            type: "POST",
            url: "http://localhost:8000/mydeck/deck",
            dataType: "json",
            headers: {
                "Authorization": 'Token '+token,
                "X-CSRFToken": csrftoken,
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
        window.location.reload()
    })

    $(".deck").click(function () {
        getdeck(this.id,function (data) {
            $('#deck').empty()
            data.forEach(function(element) {
                console.log(element.name);
                $('#deck').append("<tr><td class='deckCard' id="+element.id+">"+element.name+"</td></tr>")
            });
        })
    })
});

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

function getdeck(id,callback) {
    $.ajax({
            type: "GET",
            url: "http://localhost:8000/mydeck/deckCards/"+id,
            dataType: "json",
            headers: {
                "Authorization": 'Token '+token,
                "X-CSRFToken": csrftoken,
                "Content-Type":'application/json'
            },
            success: function (data) {
                console.log('Success!',data)
                callback(data)
            },
            error : function(err) {
                console.log('Error!', err)
            },
        });
}
