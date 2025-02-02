// ==============================
// 📌 Fetch and Render Assessment Data in Charts
// ==============================
document.addEventListener("DOMContentLoaded", function () {
    let chartCanvas = document.getElementById("assessmentChart");

    if (chartCanvas) {
        fetch("/api/assessment-visualization/")
            .then(response => response.json())
            .then(data => {
                let ctx = chartCanvas.getContext("2d");
                let chart = new Chart(ctx, {
                    type: "bar",
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: "Assessment Scores",
                            data: data.scores,
                            backgroundColor: "rgba(54, 162, 235, 0.5)",
                            borderColor: "rgba(54, 162, 235, 1)",
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            })
            .catch(error => console.error("Error fetching assessment data:", error));
    }
});

// ==============================
// 📌 Dynamic Alerts
// ==============================
function showAlert(message, type) {
    let alertContainer = document.createElement("div");
    alertContainer.className = `alert alert-${type} mt-3`;
    alertContainer.innerHTML = message;

    document.body.prepend(alertContainer);

    setTimeout(() => {
        alertContainer.remove();
    }, 3000);
}

// Example Usage
// showAlert("Data loaded successfully!", "success");
