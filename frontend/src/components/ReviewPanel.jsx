function ReviewPanel({ result }) {

  if (!result) {
    return <p>No review generated yet.</p>;
  }

  return (
    <div>
      <h2>Analysis</h2>

      <p>
        <strong>Prediction:</strong>{" "}
        {result.prediction}
      </p>

      <p>
        <strong>Confidence:</strong>{" "}
        {result.confidence}%
      </p>

      <h3>Review</h3>

      <pre
        style={{
          whiteSpace: "pre-wrap"
        }}
      >
        {result.review}
      </pre>
    </div>
  );
}

export default ReviewPanel;