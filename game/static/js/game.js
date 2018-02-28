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
    oponentHand = 5;
    token = document.getElementById("token").innerHTML;
    csrftoken = getCookie('csrftoken');

    getDeck(function (data) {
        data.forEach(function(element) {
            myDeck.push(element);
        });
        myDeck = shuffle(myDeck)
        for (i= 0; i<5; i++){
            myHand.push(myDeck[i]);
            $('#myHand').append("<span class='myHandCard' id='myHandCard-"+i+"'><input name='cardId' style='display: none' value='"+myDeck[i].id+"'><img title='"+myDeck[i].name+"' src='"+myDeck[i].img+"' style='width: 100px; height: 190px;' /></span>")
            $('#oponentHand').append("<span class='oponentHandCard' id='oppnentHandCard-" + (i+1) + "'><img title='deck' src='game\static\img\deck.png' style='width: 100px; height: 190px;' /></span>")
            delete myDeck[i];
        }
        myDeck = cleanArray(myDeck);
    },$('#deckId').val());

    getCard(function (data) {
        data.forEach(function(element) {
            cards.push(element);
        });
    });

    $(document).on('click', '.myHandCard', function () {
        console.log($(this).children('input[name="cardId"]').val())
        console.log(this.id.split('-')[1]);
        putCard(this.id.split('-')[1],$(this).children('input[name="cardId"]').val())
    });
});

function putCard(handId, cardId) {
    myBoard.push(myHand[handId]);
    $('#myBoard').append("<span class='myBoardCard' id='myBoardCard-"+myBoard.length+"'><img title='"+myHand[handId].name+"' src='"+myHand[handId].img+"' style='width: 100px; height: 190px;' /></span>")
    $("#myHandCard-"+handId+"").remove();
    delete myHand[handId];
    if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action": "put",
			"username": document.getElementById('user').innerHTML,
			"cardId": cardId
		};
		socket.send(JSON.stringify(data));
	}
}

function draw(){
    myHand.push(myDeck[0]);
    $('#myHand').append("<span class='myHandCard' id='myHandCard-"+(myHand.length-1)+"'><input name='cardId' style='display: none' value='"+myDeck[0].id+"'><img title='"+myDeck[0].name+"' src='"+myDeck[0].img+"' style='width: 100px; height: 190px;' /></span>")
    delete myDeck[0];
    myDeck = cleanArray(myDeck)
    if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action": "draw",
			"username": document.getElementById('user').innerHTML,
            "hand": myHand.length,
		};
		socket.send(JSON.stringify(data));
	}
}

function attaquer( attaquant, attaquer) {
    oponentBoard[attaquer].health = oponentBoard[attaquer].health - myBoard[attaquant].attack
}

function getDeck(callback, id="") {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + ":8000/mydeck/deckCards/"+id,
        dataType: "json",
        headers: {
            "Authorization": 'Token '+token,
            "X-CSRFToken": csrftoken,
            "Content-Type":'application/json'
        },
        success: function (data) {
            console.log('Success!')
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
        url: "http://" + window.location.host + ":8000/mydeck/card/"+id,
        dataType: "json",
        headers: {
            "Authorization": 'Token '+token,
            "X-CSRFToken": csrftoken,
            "Content-Type":'application/json'
        },
        success: function (data) {
            console.log('Success!')
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
