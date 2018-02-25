var deck = [];
var token;
var csrftoken;

$( document ).ready(function() {
    token = document.getElementById("token").innerHTML;
    csrftoken = getCookie('csrftoken');

    $(".card").on('click', function () {
        deck.push(parseInt(this.id));
        $('#newdeck').append("<tr><td class='newDeckCard' id="+this.id+">"+this.innerHTML+"</td></tr>")
    });

    $(document).on('click', "#senddeck",function () {
        var nom = $('#nomdeck').val();
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
                window.location.reload()
            },
            error : function(err) {
                console.log('Error!', err)
            }
        });
    });

    $(".deck").on('click', (function () {
        $('#modifHandler').empty();
        $('#modifHandler').append("<div id=\"modifForm\">\n" +
            "            <span id=\"deckId\"></span>\n" +
            "            <input type=\"text\" id=\"nomdeckmodif\" placeholder=\"supr\">\n" +
            "            <table id=\"deck\">\n" +
            "\n" +
            "            </table>\n" +
            "            <input type=\"button\" id=\"modifDeck\" value=\"modifier le deck\">\n" +
            "            <input type=\"button\" id=\"suprDeck\" value=\"suprimer le deck\">\n" +
            "            <input type=\"button\" id=\"annulermodif\" value=\"annuler\">\n" +
            "        </div>")
        getDeck(this.id,function (data) {
            $('#deck').empty()
            data.forEach(function(element) {
                console.log(element.name);
                $('#deck').append("<tr><td class='deckCard' id="+element.id+">"+element.name+"</td></tr>")
            });
        });
    }));

    $(document).on('click', "#annulermodif",function () {
        $("#modifHandler").empty();
    })

    $("#creation").on('click', function () {
        $("#creation").hide();
        $("#creationHandler").append("<div id=\"creationForm\"><input type=\"text\" id=\"nomdeck\" placeholder=\"nom du deck\">\n" +
            "        <table id=\"newdeck\">\n" +
            "\n" +
            "        </table>\n" +
            "        <input type=\"button\" id=\"senddeck\" value=\"crée le deck\">"+
            "        <input type=\"button\" id=\"annulerCrea\" value=\"annuler\"></div>");
    })

    $(document).on('click', "#annulerCrea",function () {
        $("#creation").show();
        $("#creationHandler").empty();
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

function getDeck(id,callback) {
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
