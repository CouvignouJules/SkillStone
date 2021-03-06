var myDeck = [];
var myHand = [];
var myBoard = [];
var duel = [];
var oponentHand;
var oponentBoard = [];
var cards = [];
var mypv;
var oponentPv;
var token;
var csrftoken;
var turn;

$( document ).ready(function() {
    mypv = 30;
    oponentPv = 30;
    oponentHand = 5;
    token = document.getElementById("token").innerHTML;
    csrftoken = getCookie('csrftoken');
    turn = false;
    $( ":button" ).prop("disabled",true);

    getDeck(function (data) {
        data.forEach(function(element) {
            myDeck.push(element);
        });
        myDeck = shuffle(myDeck)
        for (i= 0; i<5; i++){
            myHand.push(myDeck[i]);
            $('#myHand').append("<span class='myHandCard' id='myHandCard-"+i+"'><input name='cardId' style='display: none' value='"+myDeck[i].id+"'><img title='"+myDeck[i].name+"' src='http://" + window.location.host + "/" + myDeck[i].img + "' style='width: 130px; height: 190px;' /></span>")
            $('#oponentHand').append("<span class='oponentHandCard' id='oppnentHandCard-" + i + "'><img title='deck' src='http://" + window.location.host + "/static/img/deck.png' style='width: 130px; height: 190px;' /></span>")
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

    $(document).on('click', '.onBoardCard', function () {
        if (duel.length < 2){
            $(this).find('img').css('box-shadow', '10px 10px 5px #888');
            if ($(this).parent().attr('id') == "oponentBoard"){
                console.log("pasmacarte");
                duel.push(this.id.split('-')[1]);
            }else if ($(this).parent().attr('id') == "myBoard"){
                console.log("macarte");
                duel.push(this.id.split('-')[1]);
            }else {
                duel.push(this.id);
            }
        }
    });

    $('#attack-button').on('click', function () {
        attack(duel[0],duel[1]);
    })

    $('#pass-button').on('click', function () {
        $( ":button" ).prop("disabled",true);
        turn = false;
        if (socket.readyState === WebSocket.OPEN) {
            data = {
                "action": "pass",
                "username": document.getElementById('user').innerHTML
            };
            socket.send(JSON.stringify(data));
        }
    })
});

function putCard(handId, cardId) {
    myBoard.push(myHand[handId]);
    $('#myBoard').append("<span class='myBoardCard onBoardCard' id='myBoardCard-"+(myBoard.length-1)+"'><img title='"+myHand[handId].name+"' src='http://" + window.location.host + "/" + myHand[handId].img + "' style='width: 130px; height: 190px;' /></span>")
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
    $('#myHand').append("<span class='myHandCard' id='myHandCard-"+(myHand.length-1)+"'><input name='cardId' style='display: none' value='"+myDeck[0].id+"'><img title='"+myDeck[0].name+"' src='http://" + window.location.host + "/" + myDeck[0].img+"' style='width: 130px; height: 190px;' /></span>")
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

function attack( assailant, target) {
    if (target != "oponenthero"){
        oponentBoard[target].health = oponentBoard[target].health - myBoard[assailant].attack;
        myBoard[assailant].health = myBoard[assailant].health - oponentBoard[target].attack;
        if (oponentBoard[target].health <= 0){
            $("#oponentBoardCard-"+target+"").remove();
        }
        if (myBoard[assailant].health <= 0){
            $("#myBoardCard-"+assailant+"").remove();
        }
    }else{
        oponentPv -= myBoard[assailant].attack;
        $("#hero1-hp").text(oponentPv);
    }
    if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action": "attack",
			"username": document.getElementById('user').innerHTML,
			"attackingCard": assailant,
			"target": target
		};
		socket.send(JSON.stringify(data));
	}
	duel = [];
}

function getDeck(callback, id="") {
    $.ajax({
        type: "GET",
        url: "http://skillstone.thulium.ovh:8000/mydeck/deckCards/"+id,
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
        url: "http://skillstone.thulium.ovh:8000/mydeck/card/"+id,
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
