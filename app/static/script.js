const video = document.getElementById("video");
const canvas = document.getElementById("canvas") || document.createElement("canvas");
const context = canvas.getContext("2d");
const statusText = document.getElementById("status-text");

// Acceder a la cámara
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => video.srcObject = stream)
    .catch(console.error);

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
        })
        .catch(err => {
            statusText.textContent = "Error al analizar imagen.";
            console.error(err);
        });
    }, "image/jpeg");
}

// Captura y envía imágenes cada 1 segundo
setInterval(captureAndSend, 1000);
