import React, { useState } from 'react';
import axios from 'axios';
import './App.css';  
function App() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState('');

  const handleInputChange = (e) => {
    setText(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await axios.post('http://localhost:5000/predict', 
        { text },
        { headers: { 'Content-Type': 'application/json' } }
      );
      setSentiment(response.data.sentiment);
    } catch (error) {
      console.error('Error making prediction:', error.message);
      alert(`Error making prediction: ${error.message}`);
    }
  };
  
  const getSentimentClass = () => {
    switch (sentiment) {
      case 'Positive':
        return 'sentiment-positive';
      case 'Negative':
        return 'sentiment-negative';
      case 'Neutral':
        return 'sentiment-neutral';
      default:
        return '';
    }
  };
  
  return (
    <div className="App">
      <h1>Sentiment Analysis of Twitter Comments</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={text}
          onChange={handleInputChange}
          placeholder="Enter text to analyze sentiment"
        />
        <button type="submit">Analyze Sentiment</button>
      </form>
      {sentiment && <p className={getSentimentClass()}> Sentiment:</p>}
    </div>
  );
}

export default App;
