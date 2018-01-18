

socket = new WebSocket("ws://192.168.42.235:80");

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
	if(result["username"] != document.getElementById('user').innerHTML) {
        console.log(Date.now() + ' - ' + e.data);
        if (result["action"] != null) {
            switch (result["action"]) {
				case "join":
					// Connexion d'un joueur, animation en JS ?
					break;
                case "draw":
                    // L'autre joueur a draw, petite animation en JS ?
                    break;
                case "put":
                    // L'autre joueur a poser une carte, petite animation en JS ?
                    break;

                case "attack":
                    // L'autre joueur attaque, petite animation en JS ?
                    break;
                default:

                    break;
            }
        }
    }


	//test = document.getElementById("test");
	//test.value = e.data;
};

function draw(user,number){


	if (socket.readyState === WebSocket.OPEN) {
		//console.log('draw');
		data = {
			"action": "draw",
			"username": user,
			"number": number
		};
		socket.send(JSON.stringify(data));
		//socket.close();
	}




}

