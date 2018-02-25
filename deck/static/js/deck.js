var deck = [];
var token;
var csrftoken;

$( document ).ready(function() {
    $('#nomdeck').val("Nouveau Deck");
    token = document.getElementById("token").innerHTML;
    csrftoken = getCookie('csrftoken');

    $(".card").on('click', function () {
        deck.push(parseInt(this.id));
        $('#newdeck').append("<div class='newDeckCard' id="+this.id+">"+this.innerHTML+"</div>")
    });

    $("#senddeck").on('click', function () {
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

    $("#select-deck").on('change', function() {
      if($("#select-deck").val() == "") {
        $("#modifDeck").hide();
        $("#suprDeck").hide();
        $("#senddeck").show();
        $('#nomdeck').val("Nouveau Deck");
        $('#newdeck').empty()
      } else {
        $("#modifDeck").show();
        $("#suprDeck").show();
        $("#senddeck").hide();
        getDeck($("#select-deck").val(),function (data) {
            $('#newdeck').empty()
            $('#nomdeck').val($("#select-deck option:selected").text());
            data.forEach(function(element) {
                console.log(element.name);
                $('#newdeck').append("<div class='deckCard' id="+element.id+"><img title='"+element.name+"' src='"+element.img+"' style='width: 200px; height: 290px;' /></div>")
            });
        });
      }
    });
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
