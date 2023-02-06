async function handleRoomForms(token) {
    event.preventDefault();
    const formData = new FormData(event.target);
    formData.append('csrfmiddlewaretoken', token);
    const roomName = formData.get('room_name');
    const response = await fetch(`http://127.0.0.1:8000/add-room/${roomName}/`, {
        method: 'POST', body: formData
    });

    const responseData = await response.json();
    console.log(responseData);
}

async function handleEnterRoomForm(token) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const roomName = formData.get('room_name');
    const response = await fetch(`http://127.0.0.1:8000/enter-room/${roomName}/`, {
        method: 'POST', headers: {
            'Content-Type': 'application/json', 'X-CSRFToken': token, 'X-Requested-With': 'XMLHttpRequest'
        }, body: JSON.stringify({'room_name': roomName})
    });

    const responseData = await response.json();

    if (responseData === 'Entering.') {
        window.location.href = `${roomName}/`;
    } else {
        console.log(responseData);
    }

}