const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/' + roomName + '/');

chatSocket.onmessage = async function (e) {
    const data = JSON.parse(e.data);
    const info = await (await fetch('http://127.0.0.1:8000/info/get')).json();
    const [sender, date] = info.split('|');

    const message = data.message;
    const chatLog = document.querySelector('.chat-log');

    const messageBox = document.createElement('div');
    messageBox.className = 'message-box';

    const messageInfoBox = document.createElement('div');
    messageInfoBox.className = 'message-info-box';

    createElement('fa-solid fa-user', 'message-sender', sender, messageInfoBox);

    createElement('fa-solid fa-calendar-days', 'message-date', date, messageInfoBox);

    messageBox.append(messageInfoBox);

    createElement('fa-solid fa-message', 'message', message, messageBox);

    chatLog.append(messageBox);

};

chatSocket.onclose = function () {
    console.error('Chat socket closed unexpectedly');
};

async function sendMessage(senderId, roomName) {
    const messageInputDom = document.querySelector('.chat-message-input');
    const message = messageInputDom.value;
    await fetch(`http://127.0.0.1:8000/send/${message}/${senderId}/${roomName}/`);

    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
}

function createElement(iconClass, paragraphClass, content, parentElement) {
    const p = document.createElement('p');
    const i = document.createElement('i');
    i.className = iconClass;
    p.className = paragraphClass;
    p.textContent = ' ' + content;
    p.prepend(i);
    parentElement.append(p);
}