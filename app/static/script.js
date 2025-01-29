const video = document.getElementById("video");
const canvas = document.getElementById("canvas") || document.createElement("canvas");
const context = canvas.getContext("2d");
const statusText = document.getElementById("status-text");

// Cargar sonidos de alerta
const alarmSound = new Audio("static/alert.mp3");  // alarma de somnolencia


// Acceder a la cámara
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => video.srcObject = stream)
    .catch(console.error);

let lastState = "";

// Función para capturar y enviar imágenes automáticamente
function captureAndSend() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0);

    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append("image", blob, "capture.jpg");

        fetch("/detect", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            statusText.textContent = data.status;

            // Reproducir sonido solo cuando el estado cambie
            if ((data.status === "Somnoliento !" || data.status === "DORMIDO !!!") && lastState !== data.status) {
                alarmSound.play();
            }
            

            lastState = data.status; // Guardar el último estado
        })
        .catch(err => {
            statusText.textContent = "Error al analizar imagen.";
            console.error(err);
        });
    }, "image/jpeg");
}

// Captura y envía imágenes cada 1 segundo
setInterval(captureAndSend, 1000);
