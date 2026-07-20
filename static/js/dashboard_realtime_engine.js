async function fetchMetrics() {
    const res = await fetch('/metrics');
    const data = await res.json();

    document.getElementById("total").innerText = data.total_requests;
    document.getElementById("success").innerText = data.success;
    document.getElementById("errors").innerText = data.errors;
    document.getElementById("rate").innerText = data.success_rate;

    let logsHTML = "";
    data.logs.forEach(log => {
        logsHTML += `<div>[${log.time}] ${log.type} - ${log.message}</div>`;
    });

    document.getElementById("logs").innerHTML = logsHTML;
}

setInterval(fetchMetrics, 2000);
