const form = document.getElementById("askForm");
const input = document.getElementById("questionInput");
const result = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const question = input.value.trim();
    if (!question) return;

    result.innerHTML = `<p class="loading">Thinking...</p>`;

    try {
        const formData = new FormData();
        formData.append("question", question);

        const response = await fetch("/ask", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        result.innerHTML = `
            <div class="answer">
                <p class="asked"><strong>Question:</strong> ${data.question}</p>
                <p class="reply">${data.answer}</p>
                <div class="meta">
                    <span>Valid: ${data.is_valid ? "Yes" : "No"}</span>
                    <span>Attempts: ${data.retries}</span>
                </div>
            </div>
        `;
    } catch (err) {
        result.innerHTML = `
            <p class="error">
                Unable to fetch answer. Please try again later.
            </p>
        `;
    }
});