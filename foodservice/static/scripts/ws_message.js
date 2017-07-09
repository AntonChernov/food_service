/**
 * Created by tito on 09.07.17.
 */

function wsConnect () {
    socket = new WebSocket("ws://" + window.location.host + "/order_room/");
    socket.onmessage = function(e) {
        console.log(e.data);
    };
    socket.onopen = function() {
        socket.send("hello world");
    };

    if (socket.readyState == WebSocket.OPEN) socket.onopen();
}