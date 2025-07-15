chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "explain") {
    fetch("http://localhost:8000/explain", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: request.text })
    })
      .then(res => res.json())
      .then(data => {
        alert("LLM says:\n\n" + data.explanation);
      })
      .catch(err => {
        alert("Error: " + err.message);
      });
  }
});
