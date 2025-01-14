let users = []; // Lista de usuarios cargados
let currentUserIndex = 0; // Índice del usuario mostrado actualmente
// Cargar usuarios al inicio
fetch('/users/')
    .then(response => response.json())
    .then(data => {
        users = data;
        if (users.length > 0) {
            displayUser(currentUserIndex);
        } else {
            alert('No hay usuarios disponibles.');
        }
    })
    .catch(error => console.error('Error al cargar usuarios:', error));

// Mostrar el usuario actual en el HTML
function displayUser(index) {
    const user = users[index];
    document.getElementById('nombre_empresa').innerHTML = `<h1>${user.username}</h1>`;
    document.getElementById('Logo').src = `/static/${user.image_user}`;
    document.getElementById('datos_usaurio').innerHTML = `
        Direccion: ${user.direction}<br>
        Slogan: ${user.slogan}<br>
        Contacto: ${user.contacto}
    `;
}

// Cambiar al usuario anterior o siguiente
document.querySelector('.arrow-left').addEventListener('click', () => {
    if (currentUserIndex > 0) {
        currentUserIndex--;
        displayUser(currentUserIndex);
    } else {
        alert('No hay usuarios anteriores.');
    }
});

document.querySelector('.arrow-right').addEventListener('click', () => {
    if (currentUserIndex < users.length - 1) {
        currentUserIndex++;
        displayUser(currentUserIndex);
    } else {
        alert('No hay más usuarios.');
    }
});