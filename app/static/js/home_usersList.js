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
    document.getElementById('name_user').innerHTML = user.username;
    document.getElementById('Logo').src = `/static/${user.image_user}`;
    document.getElementById('datos_usaurio').innerHTML = `
        <p><span>Dirección</span>: ${user.direction}</p>
        <p><span>Slogan:</span> ${user.slogan}</p>
        <p><span>Contacto:</span> ${user.contacto}</p>
    `;
    var text = `https://wa.me/${user.contacto}?text=Hola%20vengo%20de%20*¿alguienSabe?*%20me%20gustaría%20saber%20más%20sobre%20sus%20servicios.`;
    document.getElementById('contact').href = text;

    function updateStatus() {
        const button_status = document.getElementById("statusButton");
        if (user.status) { //True or False
            button_status.innerHTML = "<strong>Abierto</strong><span>🟢</span>";
        } else {
            button_status.innerHTML = "<strong>Cerrado</strong><span>🔴</span>";
        }
        console.log("Actualizado");
    }
    updateStatus();  // Ejecutar al cargar la página
    setInterval(updateStatus, 18000000); //18mill/s = 5horas
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
