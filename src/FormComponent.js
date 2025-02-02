import React, { useState } from 'react';
import axios from 'axios';

const FormComponent = ({ onSubmit }) => {
  const [input, setInput] = useState(''); // State to manage form input

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://127.0.0.1:8000/api/endpoint/', { input }); // Replace with your API endpoint
      alert('Data submitted successfully!');
      setInput(''); // Clear input field
      onSubmit(); // Call parent function to refresh data
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Enter Data:
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)} // Update input state
          placeholder="Type something..."
        />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
};

export default FormComponent;
