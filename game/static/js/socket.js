

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
                    }
                    /*}*/
                    break;

                case "draw":
                    console.log("prout");
                    // L'autre joueur a draw, petite animation en JS ?
                    if (result["username"] != document.getElementById('user').innerHTML) {
                        console.log(result["username"] + " pioche une carte");
                        oponentHand += 1;
                    	console.log("pk sa affiche pas")
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
								$('#oponentBoard').append("<span class='oponentBoardCard' id='oponentBoardCard-"+oponentBoard.length+"'><img title='"+element.name+"' src='"+element.img+"' style='width: 100px; height: 190px;' /></span>");
							}
						})
						$("#oponentHandCard-0").remove()
						oponentHand -=1;
						console.log(result["username"] + " pose la carte ");
					}
                    break;

                case "attack":
                    // L'autre joueur attaque, petite animation en JS ?
                    // MAJ pdv joueur/carte, carte dead ou pas, fin partie ou pas
                    console.log(result["username"] + " attaque avec ");
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


function attack(user,attackingCard,target){
	console.log("attack");

	if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action": "attack",
			"username": document.getElementById('user').innerHTML,
			"attackingCard": attackingCard,
			"target": target
		};
		socket.send(JSON.stringify(data));
	}
}

