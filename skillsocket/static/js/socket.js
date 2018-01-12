

socket = new WebSocket("ws://127.0.0.1:8000");

socket.onopen = function() {
	/* Méthode appelée juste après la connexion */
	if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action":"join",
			"username":document.getElementById('user').innerHTML,
			"password":'doe'
		};
		socket.send(JSON.stringify(data));
		//socket.close();
	}

};


socket.onmessage = function(e) {
	/* A la réception d'un message */

	if(e.data["username"] != document.getElementById('user'))
		console.log(Date.now() + ' - ' + e.data);
	if(e.data['action']!=null) {
        switch (e.data['action']) {
			  case "draw":
				// Instructions à exécuter lorsque le résultat
				// de l'expression correspond à valeur1
				// L'autre joueur a draw, petite animation en JS ?
				break;
			  case "put":
				// Instructions à exécuter lorsque le résultat
				// de l'expression correspond à valeur2
				// L'autre joueur a poser une carte, petite animation en JS ?
				break;

			  case "attack":
				// Instructions à exécuter lorsque le résultat
				// de l'expression à valeurN
				// L'autre joueur attaque, petite animation en JS ?
				break;
			  default:
				// Instructions à exécuter lorsqu'aucune des valeurs
				// ne correspond

				break;
			}
	}


	//test = document.getElementById("test");
	//test.value = e.data;
};

function test(){


	if (socket.readyState === WebSocket.OPEN) {
		data = {
			"action":"join",
			"username":"John",
			"password":'doe'
		};
		socket.send(JSON.stringify(data));
		//socket.close();
	}




}

