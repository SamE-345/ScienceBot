document.getElementById("submit").addEventListener("click", async () => {
  const text = document.getElementById("input").value;
  const res = await fetch("http://localhost:8000/explain", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  const data = await res.json();
  if (data.explanation) {
    const outputDiv = document.getElementById("output");
    outputDiv.innerHTML = data.explanation;
    if (window.MathJax && window.MathJax.typesetPromise) {
      MathJax.typesetPromise([outputDiv]);
    }
  } else if (data.error) {
    document.getElementById("output").innerText = "Error: " + data.error + (data.details ? "\n" + JSON.stringify(data.details) : "");
  } else {
    document.getElementById("output").innerText = "Unexpected response from server.";
  }
});
