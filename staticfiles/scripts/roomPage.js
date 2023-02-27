const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/' + roomName + '/');

chatSocket.onmessage = async function (e) {
    const data = JSON.parse(e.data);
    const info = await (await fetch('http://127.0.0.1:8000/info/get')).json();
    const [sender, date, loggedUser, messageId] = info.split('|');
    const action = data.action;

    if (action === 'delete') {
        fetch(`http://127.0.0.1:8000/delete-message/${messageId}/`);
        const el = document.getElementById(`${data.message}`).parentElement;
        el.remove();
    } else {
        const message = data.message;
        const chatLog = document.querySelector('.chat-log');

        const messageBox = document.createElement('div');
        messageBox.className = 'message-box';

        const messageInfoBox = document.createElement('div');
        messageInfoBox.className = 'message-info-box';

        createElement('fa-solid fa-user', 'message-sender', sender, messageInfoBox);

        createDeleteBtn(messageInfoBox, messageId, loggedUser, sender);

        createElement('fa-solid fa-calendar-days', 'message-date', date, messageInfoBox);

        messageBox.append(messageInfoBox);

        createElement('fa-solid fa-message', 'message', message, messageBox);

        chatLog.append(messageBox);
    }
};

chatSocket.onclose = function () {
    console.error('Chat socket closed unexpectedly');
};

async function sendMessage(senderId, roomName) {
    const messageInputDom = document.querySelector('.chat-message-input');
    const message = messageInputDom.value;
    messageInputDom.value = 'Sending...'
    await fetch(`http://127.0.0.1:8000/send/${message}/${senderId}/${roomName}/`);

    chatSocket.send(JSON.stringify({
        'message': message, 'action': 'send',
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

function createDeleteBtn(parentEl, messageId, loggedUser, sender) {
    const actionParagraph = document.createElement('p');
    actionParagraph.className = 'action-btns';

    const deleteBtn = document.createElement('i');
    deleteBtn.title = 'delete';
    deleteBtn.classList.add('fa-solid', 'fa-trash');

    if (loggedUser === sender) {
        actionParagraph.append(deleteBtn);
        parentEl.append(actionParagraph);
    }

    parentEl.id = messageId;

    deleteBtn.onclick = () => {
        chatSocket.send(JSON.stringify({
            'message': `${messageId}`, 'action': 'delete',
        }));
    }
}

function deleteMessage(messageId) {
    // This function is attached to the delete button while rendering the template

    chatSocket.send(JSON.stringify({
        'message': `${messageId}`, 'action': 'delete',
    }));
}
