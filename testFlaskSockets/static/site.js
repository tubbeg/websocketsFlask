//file should ideally be served by nginx/apache instead of flask
$('document').ready(() => {
    document.getElementById("sendButton").disabled = true;
    var socket = io();
    socket.on('connect', () => {
        document.getElementById("sendButton").disabled = false;
        function updateList(myText){
          let ul = document.getElementById("myList");
          let li = document.createElement("li");
          li.appendChild(document.createTextNode(myText));
          ul.appendChild(li);
        }
        function sendMessage(){
            let myText = document.getElementById('messageInput').value;
            if (myText == "")
                return;
            updateList(myText);
            document.getElementById('messageInput').value = "";
            socket.emit('messageEvent', {message: myText});
            console.log("sent: " + myText);
        }
        document.getElementById("sendButton").addEventListener("click", sendMessage);
    });
});