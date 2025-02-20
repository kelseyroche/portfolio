import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("https://portfolio-2sie.onrender.com/ping")
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  return <h1>Backend says: {message}</h1>;
}

export default App;