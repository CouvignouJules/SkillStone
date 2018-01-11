

socket = new WebSocket("ws://localhost:8000");

socket.onopen = function() {
	/* Méthode appelée juste après la connexion */

	// TODO : player name
	socket.send("* Patou vient de se connecter");
};


socket.onmessage = function(e) {
	/* A la réception d'un message */
	console.log(Date.now() + ' - ' + e.data);

	Document.getElementById('test').innerHTML(e.data);
};

function test(){


	if (socket.readyState === WebSocket.OPEN) {
		data = {
		"action":"join",
		"username":"John",
		"password":'doe'
		};
		socket.send(JSON.stringify(data));
		socket.close();
	}



}