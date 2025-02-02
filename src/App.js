import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import axios from "axios";
import Dashboard from "./pages/Dashboard";
import Profile from "./pages/Profile";
import Chatbot from "./components/Chatbot";

const Home = () => {
  const [data, setData] = useState(null);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch data from Django backend
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/endpoint/");
        setData(response.data);
      } catch (err) {
        setError("Failed to fetch data. Please try again.");
      }
      setLoading(false);
    };
    fetchData();
  }, []);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await axios.post("http://127.0.0.1:8000/api/submit/", { input });
      alert("Data submitted successfully!");
      setInput("");
      const updatedData = await axios.get("http://127.0.0.1:8000/api/endpoint/");
      setData(updatedData.data);
    } catch (err) {
      setError("Failed to submit data. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-blue-600 mb-4">CSA Sports Performance Tracker</h1>

      {/* Display Backend Message */}
      {data ? <p className="text-lg text-gray-700">Backend Message: {data.message}</p> : <p>Loading...</p>}

      {/* Form Section */}
      <form 
        onSubmit={handleSubmit} 
        className="bg-white shadow-md rounded-lg p-6 w-full max-w-md"
      >
        <label className="block text-gray-700 text-sm font-bold mb-2">
          Enter Data:
        </label>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type something..."
          className="w-full p-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-400"
        />
        <button 
          type="submit" 
          className="w-full mt-3 bg-blue-500 text-white p-2 rounded-lg hover:bg-blue-600 transition"
        >
          Submit
        </button>
      </form>

      {/* Loading and Error Handling */}
      {loading && <p className="mt-4 text-blue-500 font-semibold">Loading...</p>}
      {error && <p className="mt-4 text-red-500 font-semibold">{error}</p>}
    </div>
  );
};

const App = () => {
  return (
    <Router>
      {/* Updated Navigation Bar - Vertical Layout */}
      <nav className="flex flex-col items-center bg-gray-800 text-white p-4 space-y-4">
        <Link to="/" className="text-lg hover:text-blue-400">Home</Link>
        <Link to="/dashboard" className="text-lg hover:text-blue-400">Dashboard</Link>
        <Link to="/profile" className="text-lg hover:text-blue-400">Profile</Link>
        <Link to="/chatbot" className="text-lg hover:text-blue-400">Chatbot</Link>
      </nav>

      {/* Routes */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/chatbot" element={<Chatbot />} />
      </Routes>
    </Router>
  );
};

export default App;
