const button =
document.getElementById(
  "analyzeBtn"
);

button.addEventListener(
  "click",
  async () => {

    const resultDiv =
      document.getElementById(
        "result"
      );

    resultDiv.innerHTML =
      "Loading selected code...";

    const data =
      await chrome.storage.local.get(
        "selectedCode"
      );

    const code =
      data.selectedCode;

    if (!code) {

      resultDiv.innerHTML =
        "No code selected.";

      return;
    }

    resultDiv.innerHTML =
      "Analyzing...";

    try {

      const response =
        await fetch(
          "http://127.0.0.1:8000/review",
          {
            method: "POST",

            headers: {
              "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
              code
            })
          }
        );

      const result =
        await response.json();

      resultDiv.innerHTML = `
<h3>Prediction: ${result.prediction}</h3>
<p><b>Confidence:</b> ${result.confidence}%</p>
<pre>${result.review}</pre>
`;
    } catch (error) {

      resultDiv.innerHTML =
        "Backend not running.";
    }
  }
);