

socket = new WebSocket("ws://" + window.location.host);

socket.onopen = function() {
	console.log("join")
	if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action":"join",
			"username":document.getElementById('user').innerHTML,
            "hand": myHand.length,
		};
		socket.send(JSON.stringify(data));
		//socket.close();
	}
};


socket.onmessage = function(e) {
	var result = JSON.parse(e.data);
	/* A la réception d'un message */
        if (result["action"] != null) {
            switch (result["action"]) {
                case "join":
                    /*if (result["gameIsFull"]) {
                        console.log("Game is full");
                    }
                    else {*/
                    if (result["username"] != document.getElementById('user').innerHTML) {
                        // Connexion d'un joueur, animation en JS ?
                        console.log("Bienvenue " + result["username"]); // debug ..
                        turn = true;
                        $( ":button" ).prop("disabled",false);
                    }

                    /*}*/
                    break;

                case "draw":
                    // L'autre joueur a draw, petite animation en JS ?
                    if (result["username"] != document.getElementById('user').innerHTML) {
                        console.log(result["username"] + " pioche une carte");
                        oponentHand += 1;
                    }
                    if (result["username"] != document.getElementById('user').innerHTML) {
                        $('#oponentHand').append("<span class='oponentHandCard' id='oppnentHandCard-" + oponentHand + "'><img title='deck' src='game\static\img\deck.png' style='width: 100px; height: 190px;' /></span>")
                    }
                    break;

                case "put":
                    // L'autre joueur a poser une carte, petite animation en JS ?
					if (result["username"] != document.getElementById('user').innerHTML) {
						cards.forEach(function(element) {
							if(element.id == result["cardId"]){
								oponentBoard.push(element);
								$('#oponentBoard').append("<span class='oponentBoardCard onBoardCard' id='oponentBoardCard-"+(oponentBoard.length-1)+"'><img title='"+element.name+"' src='"+element.img+"' style='width: 100px; height: 190px;' /></span>");
							}
						})
						$("#oppnentHandCard-"+(oponentHand)+"").remove()
						oponentHand -=1;
						console.log(result["username"] + " pose la carte ");
					}
                    break;

                case "attack":
                    // L'autre joueur attaque, petite animation en JS ?
                    // MAJ pdv joueur/carte, carte dead ou pas, fin partie ou pas
                    console.log(result["username"] + " attaque avec ");
                    if (result["username"] != document.getElementById('user').innerHTML){
                        if (result["target"] != "oponenthero") {
                            myBoard[result["target"]].health = myBoard[result["target"]].health - oponentBoard[result["attackingCard"]].attack;
                            oponentBoard[result["attackingCard"]].health = oponentBoard[result["attackingCard"]].health - myBoard[result["target"]].attack;
                            if (oponentBoard[result["attackingCard"]].health <= 0) {
                                $("#oponentBoardCard-" + result["attackingCard"] + "").remove();
                            }
                            if (myBoard[result["target"]].health <= 0) {
                                $("#myBoardCard-" + result["target"] + "").remove();
                            }
                        }else {
                            console.log()
                            mypv -= oponentBoard[result["attackingCard"]].attack;
										        $("#hero2-hp").text(mypv);
                        }
                        duel = [];
                    }
                    break;
                case "pass":
                    if (result["username"] != document.getElementById('user').innerHTML) {
                        console.log(result["username"] + " passe son tour");
                        turn = true;
                        draw();
                        $( ":button" ).prop("disabled",false);
                    }
                    // L'autre joueur passe son tour
                    break;
                default:
                    break;
            }
		}

};

socket.onclose = function(e) {
	data = {
		"action": "disconnect",
		"username": document.getElementById('user').innerHTML,
	};
	socket.send(JSON.stringify(data));
};
