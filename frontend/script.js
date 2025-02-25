function generateCode() {
    const prompt = document.getElementById("prompt").value;
    const language = document.getElementById("language").value;
    
    fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, language })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("codeResult").innerText = data.optimized_code;
    })
    .catch(error => console.error("Ошибка:", error));
}
