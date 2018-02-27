var myDeck = [];
var myHand = [];
var myBoard = [];
var oponentDeck;
var oponentHand;
var oponentBoard = [];
var cards = [];
var pv;
var token;
var csrftoken;

$( document ).ready(function() {
    pv = 30;
    token = document.getElementById("token").innerHTML;
    csrftoken = getCookie('csrftoken');

    getDeck(function (data) {
        data.forEach(function(element) {
            myDeck.push(element);
        });
        myDeck = shuffle(myDeck)
        console.log(myDeck)
        for (i= 0; i<5; i++){
            myHand.push(myDeck[i])
            delete myDeck[i];

        }
        myDeck = cleanArray(myDeck)
        console.log("main");
        console.log(myHand);
        console.log("deck");
        console.log(myDeck);
    },$('#deckId').val());

    getCard(function (data) {
        data.forEach(function(element) {
            cards.push(element);
        });
    });
});


function getDeck(callback, id="") {
    $.ajax({
        type: "GET",
        url: "http://192.168.1.31:8000/mydeck/deckCards/"+id,
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

function getCard(callback, id="") {
    $.ajax({
        type: "GET",
        url: "http://192.168.1.31:8000/mydeck/card/"+id,
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

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
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