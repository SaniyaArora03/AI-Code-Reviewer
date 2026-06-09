import { useState } from "react";
import axios from "axios";

import CodeEditor from "./components/CodeEditor";
import ReviewPanel from "./components/ReviewPanel";

import "./App.css";

function App() {

  const [code, setCode] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const reviewCode = async () => {

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/review",
        {
          code
        }
      );

      setResult(
        response.data
      );

    } catch (error) {

      console.error(error);

      alert("Backend Error");

    } finally {

      setLoading(false);
    }
  };

  return (
    <div className="container">

      <div className="left-panel">

        <CodeEditor
          code={code}
          setCode={setCode}
        />

        <button
          onClick={reviewCode}
        >
          {
            loading
              ? "Reviewing..."
              : "Review Code"
          }
        </button>

      </div>

      <div className="right-panel">

        <ReviewPanel
          result={result}
        />

      </div>

    </div>
  );
}

export default App;