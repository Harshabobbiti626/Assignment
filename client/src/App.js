import React from 'react';
import BMICalculator from './components/BMICalculator';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>BMI Calculator</h1>
      </header>
      <main>
        <BMICalculator />
      </main>
    </div>
  );
}

export default App;
