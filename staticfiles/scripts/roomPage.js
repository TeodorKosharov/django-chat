const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/' + roomName + '/');

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};

chatSocket.onclose = function () {
    console.error('Chat socket closed unexpectedly');
};

function sendMessage(user) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value + `[${user}]`;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
}
