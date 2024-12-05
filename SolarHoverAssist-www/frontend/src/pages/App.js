import React, { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/api/status")
      .then((response) => response.json())
      .then((data) => setStatus(data.status))
      .catch((error) => console.error("Error fetching status:", error));
  }, []);

  return (
    <div>
      <h1>Solar Hover Assist</h1>
      <p>Backend Status: {status}</p>
    </div>
  );
}

export default App;
