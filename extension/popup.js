document.getElementById("submit").addEventListener("click", async () => {
  const text = document.getElementById("input").value;
  const res = await fetch("http://localhost:8000/explain", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  const data = await res.json();
  document.getElementById("output").innerText = data.explanation;
});
