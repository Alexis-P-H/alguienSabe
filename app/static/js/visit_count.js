// Ejecutar cuando la página cargue
if (typeof Storage !== "undefined") {
    const VISIT_COUNT_KEY = "visitCount";

    let visitCount = parseInt(sessionStorage.getItem(VISIT_COUNT_KEY)) || 0;
    sessionStorage.setItem(VISIT_COUNT_KEY, ++visitCount);
    console.log("Número de visitas:", visitCount);
}

// Función para obtener la información del usuario
function getUserInfo() {
    const userInfo = {
        numberVisit: parseInt(sessionStorage.getItem("visitCount")) || 0, // Recuperar visitas
        userAgent: navigator.userAgent,  // Navegador y SO
        screenWidth: screen.width,       // Ancho de pantalla
        screenHeight: screen.height,     // Alto de pantalla
        language: navigator.language,    // Idioma del navegador
        timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,  // Zona horaria
    };
    return userInfo;
}

async function sendUserInfo() {
    const API_BASE_URL = (window.location.hostname === "127.0.0.1")
    ? "http://127.0.0.1:5000"
    : "https://alguiensabe-1.onrender.com";

    const mapUserInfo = getUserInfo();
    console.log("Enviando información del usuario:", JSON.stringify(mapUserInfo));

    try {
        const response = await fetch(`${API_BASE_URL}/save-user-info`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(mapUserInfo), // Convertir el objeto a JSON
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`HTTP ${response.status}: ${errorText}`);
        }

        const data = await response.json();
        console.log("Servidor responde:", data);
    } catch (error) {
        console.error("Error en fetch:", error);
    }
}

window.onload = function() {
    sendUserInfo();
    console.log("La página se ha cargado completamente.");
};
