function CodeEditor({ code, setCode }) {
  return (
    <div>
      <h2>Enter Code</h2>

      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your code here..."
        rows={20}
        style={{
          width: "100%",
          fontFamily: "monospace",
          fontSize: "14px"
        }}
      />
    </div>
  );
}

export default CodeEditor;