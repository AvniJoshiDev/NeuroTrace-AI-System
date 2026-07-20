async function loadAdvanced() {
    const res = await fetch('/metrics');
    const data = await res.json();

    document.getElementById("health").innerText = data.health;
    document.getElementById("prediction").innerText = data.prediction;

    let anomalyHTML = "";
    data.anomalies.forEach(a => {
        anomalyHTML += `<div>${a}</div>`;
    });

    document.getElementById("anomalies").innerHTML = anomalyHTML;
}

setInterval(loadAdvanced, 2000);
