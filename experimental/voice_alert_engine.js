function speakAlert(message) {
    const speech = new SpeechSynthesisUtterance(message);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}

async function checkAlerts() {
    const res = await fetch('/metrics');
    const data = await res.json();

    if (data.errors > 5) {
        speakAlert("Warning! High error rate detected");
    }
}

setInterval(checkAlerts, 5000);
