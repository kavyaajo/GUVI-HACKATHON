document.getElementById("sendMessage").addEventListener("click", () => {
    let userMessage = document.getElementById("userInput").value;

    console.log("Sending message:", userMessage);  // Debugging log

    fetch("/chat", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => {
        console.log("Response status:", response.status);
        return response.json();
    })
    .then(data => {
        console.log("Server response:", data);
        document.getElementById("responseText").innerText = data.response;
    })
    .catch(error => console.error("Error:", error));
});
