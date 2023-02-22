const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/' + roomName + '/');

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const chatLog = document.querySelector('.chat-log');
    const newMessage = document.createElement('p');
    newMessage.textContent = data.message;
    chatLog.append(newMessage);

};

chatSocket.onclose = function () {
    console.error('Chat socket closed unexpectedly');
};

async function sendMessage(sender, roomName) {
    const messageInputDom = document.querySelector('.chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
    await fetch(`http://127.0.0.1:8000/send/${message}/${sender}/${roomName}/`);
}
