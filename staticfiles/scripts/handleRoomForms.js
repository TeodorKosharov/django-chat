async function handleCreateRoomForm(event, token) {
    event.preventDefault();
    const formData = new FormData(event.target);
    formData.append('csrfmiddlewaretoken', token);
    const roomName = formData.get('room_name');
    const response = await fetch(`http://127.0.0.1:8000/add-room/${roomName}/`, {
        method: 'POST', body: formData
    });
    event.target.reset();
    const responseData = await processingResponse(response);

    if (responseData === `Chat room with name ${roomName} added successfully!`) {
        const availableRoomsBox = document.querySelector('.available-rooms-inner-box');
        const addedRoomLink = document.createElement('a');
        addedRoomLink.className = 'room-link';
        addedRoomLink.href = `${roomName}/`;
        addedRoomLink.textContent = roomName;
        availableRoomsBox.append(addedRoomLink);
        Swal.fire({
            title: 'Success!', text: responseData, icon: 'success', buttonsStyling: false
        });
    } else if (responseData === `Chat room with name ${roomName} already exists.`) {
        Swal.fire({
            title: 'Fail!', text: responseData, icon: 'error', buttonsStyling: false
        });
    }
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

    const responseData = await processingResponse(response);

    if (responseData === 'Entering.') {
        window.location.href = `${roomName}/`;
    } else if (responseData === `Chat room with name ${roomName} does not exists!`) {
        Swal.fire({
            title: 'Room not found!', text: `${responseData}`, icon: 'question', buttonsStyling: false
        });
    }
}

async function processingResponse(response) {
    // If the response is not valid json, SyntaxError is raised. This is because
    // of the login_required decorator - if the user is not logged in, then a json
    // response is not returned. In this case we have to redirect to login url

    try {
        return await response.json();
    } catch (SyntaxError) {
        window.location.href = 'account/login/';
    }
}