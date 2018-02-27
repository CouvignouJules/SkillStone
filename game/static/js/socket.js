

socket = new WebSocket("ws://" + window.location.host);

socket.onopen = function() {
	/* Méthode appelée juste après la connexion */
	if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action":"join",
			"username":document.getElementById('user').innerHTML
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
					if (result["gameIsFull"]) {
                        console.log("Game is full");
                    }
                    else {
                        if (result["username"] != document.getElementById('user').innerHTML) {
                            // Connexion d'un joueur, animation en JS ?
                            console.log("Bienvenue " + result["username"]); // debug ..
                        }
                    }
					break;

                case "draw":
                    // L'autre joueur a draw, petite animation en JS ?
					console.log(result["username"] + " pioche une carte");
                    break;

                case "put":
                    // L'autre joueur a poser une carte, petite animation en JS ?
					console.log(result["username"] + " pose la carte ");
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

function draw(number){
	console.log("draw");

	if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action": "draw",
			"username": document.getElementById('user').innerHTML,
			"number": number
		};
		socket.send(JSON.stringify(data));
	}
}

function put(card){
	console.log("put");

	if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action": "put",
			"username": document.getElementById('user').innerHTML,
			"card": card
		};
		socket.send(JSON.stringify(data));
	}




}

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

