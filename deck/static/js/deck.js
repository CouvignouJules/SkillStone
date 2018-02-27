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
        sendDeck(data)
    });

    $("#select-deck").on('change', function() {
        if($("#select-deck").val() == "") {
            deck = [];
            $("#modifDeck").hide();
            $("#suprDeck").hide();
            $("#senddeck").show();
            $('#nomdeck').val("Nouveau Deck");
            $('#newdeck').empty()
        } else {
            deck = [];
            $("#modifDeck").show();
            $("#suprDeck").show();
            $("#senddeck").hide();
            getDeck($("#select-deck").val(),function (data) {
                $('#newdeck').empty()
                $('#nomdeck').val($("#select-deck option:selected").text());
                var contCart = 0
                data.forEach(function(element) {
                    console.log(element.name);
                    deck.push(parseInt(element.id));
                    $('#newdeck').append("<div class='deckCard' id='card-"+contCart+"'><img title='"+element.name+"' src='"+element.img+"' style='width: 200px; height: 290px;' /></div>")
                    contCart += 1;
                });
            });
        }
    });

    $(document).on('click', '.deckCard', function () {
        var id = this.id;
        id = id.split('-')[1];
        delete deck[id];
        $('#card-' + id).remove();
    });

    $("#suprDeck").on('click', function () {
        suprDeck($('#select-deck').val());
    });
    
    $("#modifDeck").on('click', function () {
        var nom = $('#nomdeck').val();
        deck = cleanArray(deck);
        var jsondeck = JSON.stringify(deck);
        var data = "{\"name\":\""+nom+"\",\"cards\":"+jsondeck+"}";
        sendDeck(data);
        suprDeck($('#select-deck').val());
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

function  suprDeck(id) {
    $.ajax({
        type: "DELETE",
        url: "http://localhost:8000/mydeck/deck/"+id,
        dataType: "json",
        headers: {
            "Authorization": 'Token '+token,
            "X-CSRFToken": csrftoken,
            "Content-Type":'application/json'
        },
        success: function (msg) {
            console.log('Success! deck creer',msg)
            window.location.reload()
        },
        error : function(err) {
            console.log('Error!', err)
        }
    });
}

function sendDeck(data) {
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
                console.log('Success! deck suprimer',msg)
                window.location.reload()
            },
            error : function(err) {
                console.log('Error!', err)
            }
        });
}

function cleanArray(actual) {
  var newArray = new Array();
  for (var i = 0; i < actual.length; i++) {
    if (actual[i]) {
      newArray.push(actual[i]);
    }
  }
  return newArray;
}