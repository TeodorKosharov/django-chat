function deleteRoom(event, roomName) {
    fetch(`http://127.0.0.1:8000/account/delete-room/${roomName}`);
    event.target.parentElement.remove();
    Swal.fire({
        title: 'Success!', text: `Room ${roomName} deleted successfully!`, icon: 'success', buttonsStyling: false
    });
}

function enterRoom(roomName) {
    window.location.href = `http://127.0.0.1:8000/${roomName}`;
}
