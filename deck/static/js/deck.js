var deck = [];
var token;
var csrftoken;

$( document ).ready(function() {
    console.log(window.location.host);
    $('#nomdeck').val("Nouveau Deck");
    token = document.getElementById("token").innerHTML;
    console.log(token);
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
            $("#nomdeck").show();
            $("#modifDeck").hide();
            $("#suprDeck").hide();
            $("#senddeck").show();
            $('#nomdeck').val("Nouveau Deck");
            $('#newdeck').empty()
        } else if($("#select-deck").val() == "open"){
            deck = [];
            $('#newdeck').empty()
            $("#nomdeck").hide();
            $("#senddeck").hide();
            $("#modifDeck").hide();
            $("#suprDeck").hide();
            $("#openPack").show();
        } else {
            deck = [];
            $("#nomdeck").show();
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

    $("#openPack").on('click', function () {
        $('#newdeck').empty()
        for (var i = 0; i<5; i++) {
            deck.push(parseInt(Math.floor((Math.random() * 20) + 1)));
        }
        console.log(deck);
        for (var i = 0; i<deck.length; i++) {
            getCard(deck[i], function (data) {
                $('#newdeck').append("<div class='deckCard' id='newcard"+i+"'><img title='"+data[0].name+"' src='"+data[0].img+"' style='width: 200px; height: 290px;' /></div>")
            })
        }
        var jsondeck = JSON.stringify(deck);
        var data = "{\"deck\":"+jsondeck+"}";
        console.log(data);
        addCard(data);
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
    console.log(cookieValue);
    return cookieValue;
}

function getDeck(id,callback) {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + "/mydeck/deckCards/"+id,
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
        url: "http://" + window.location.host + "/mydeck/deck/"+id,
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

function getCard(id,callback) {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + "/mydeck/card/"+id,
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

function addCard(data) {
    $.ajax({
        type: "PUT",
        url: "http://" + window.location.host + "/mydeck/cardCollection",
        dataType: "json",
        headers: {
            "Authorization": 'Token '+token,
            "X-CSRFToken": csrftoken,
            "Content-Type":'application/json'
        },
        data : data,
        success: function (msg) {
            console.log('Success! card added',msg)
        },
        error : function(err) {
            console.log('Error! card pas added', err)
        }
    });
}

function sendDeck(data) {
    $.ajax({
        type: "POST",
        url: "http://" + window.location.host + "/mydeck/deck",
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