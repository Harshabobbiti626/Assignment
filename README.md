# Assignment
# BMI Calculator API

A simple Flask-based API that calculates Body Mass Index (BMI) based on weight and height inputs.

## Overview

This API provides a simple way to calculate BMI by sending weight and height values. It returns the calculated BMI value and the corresponding category (Underweight, Normal weight, Overweight, or Obese).

## Features

- Calculate BMI based on weight and height
- Get BMI category classification
- Cross-origin resource sharing (CORS) enabled
- Comprehensive error handling
- API health check endpoint
- Logging to both console and file

## Requirements

- Python 3.6+
- Flask
- Flask-CORS

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/bmi-calculator-api.git
cd bmi-calculator-api
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required packages:

```bash
pip install flask flask-cors
```

## Running the Application

Start the API server:
make sure the path you currently is in \assign\api
```bash
python api/app.py
```
Start the react client:
make sure the path you currently is in \assign\client
```bash
npm start client
```

The API will be available at http://127.0.0.1:5000/

## API Endpoints

### Health Check
- **URL**: `/`
- **Method**: `GET`
- **Response**: Information about available endpoints

### Calculate BMI
- **URL**: `/calculate-bmi`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
    "weight": 70,    // Weight in kilograms
    "height": 1.75   // Height in meters
  }
  ```
- **Success Response**:
  ```json
  {
    "bmi": 22.86,
    "category": "Normal weight"
  }
  ```
- **Error Response**:
  ```json
  {
    "error": "Missing required fields: weight and height"
  }
  ```

### List All Routes (Debug)
- **URL**: `/routes`
- **Method**: `GET`
- **Response**: List of all available routes and their methods

### Test Endpoint
- **URL**: `/test`
- **Method**: `GET`
- **Response**: Simple test message

## Example Usage

Using curl:

```bash
curl -X POST http://localhost:5000/calculate-bmi \
  -H "Content-Type: application/json" \
  -d '{"weight": 70, "height": 1.75}'
```

Using Python requests:

```python
import requests

response = requests.post(
    "http://localhost:5000/calculate-bmi",
    json={"weight": 70, "height": 1.75}
)
print(response.json())
```

## BMI Categories

- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 25
- Overweight: 25 ≤ BMI < 30
- Obese: BMI ≥ 30

## Logging

The application logs information to both the console and a file located at `/var/log/bmi-api.log`. 
Note: You may need to create this directory with appropriate permissions or modify the log path in the code.
