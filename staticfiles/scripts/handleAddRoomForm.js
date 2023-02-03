async function handleAddRoomForm(token) {
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