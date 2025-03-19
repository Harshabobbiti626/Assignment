import React, { useState } from 'react';
import './BMICalculator.css';

const BMICalculator = () => {
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const API_URL = 'http://127.0.0.1:5000';

  const calculateBMI = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      // First, check if API is accessible
      const healthCheck = await fetch(API_URL);
      if (!healthCheck.ok) {
        throw new Error('API is not accessible');
      }

      const response = await fetch(`${API_URL}/calculate-bmi`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          weight: parseFloat(weight),
          height: parseFloat(height)
        })
      });
      
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to calculate BMI');
      }
      
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
      setError(error.message);
      setResult(null);
    }
  };

  return (
    <div className="calculator-container">
      <form onSubmit={calculateBMI}>
        <div className="input-group">
          <label htmlFor="weight">Weight (kg)</label>
          <input
            id="weight"
            type="number"
            value={weight}
            onChange={(e) => setWeight(e.target.value)}
            step="0.1"
            min="0"
            required
          />
        </div>
        
        <div className="input-group">
          <label htmlFor="height">Height (m)</label>
          <input
            id="height"
            type="number"
            value={height}
            onChange={(e) => setHeight(e.target.value)}
            step="0.01"
            min="0"
            required
          />
        </div>
        
        <button type="submit">Calculate BMI</button>
      </form>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {result && (
        <div className="result">
          <h2>Your BMI Results</h2>
          <div className="bmi-value">{result.bmi}</div>
          <div className="category">{result.category}</div>
        </div>
      )}
    </div>
  );
};

export default BMICalculator;