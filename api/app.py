from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import sys
import os

# Create logs directory
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(os.path.join(log_dir, 'bmi-api.log'))
    ]
)

app = Flask(__name__)
CORS(app)

# ✅ API Health Check Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "API is running",
        "message": "Use the /calculate-bmi endpoint to calculate BMI",
        "endpoints": {
            "bmi": "/calculate-bmi (POST)",
            "routes": "/routes (GET) - Debugging"
        }
    }), 200

# ✅ Debug Route - List All Active Routes
@app.route("/routes", methods=["GET"])
def show_routes():
    routes = {rule.rule: list(rule.methods) for rule in app.url_map.iter_rules()}
    return jsonify(routes), 200
    
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test route is working!"}), 200

# ✅ BMI Calculation API
@app.route("/calculate-bmi", methods=["POST"])
def calculate_bmi():
    try:
        # Check if JSON data is provided
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        # Validate required fields
        if "weight" not in data or "height" not in data:
            return jsonify({"error": "Missing required fields: weight and height"}), 400

        weight = float(data["weight"])  # weight in kg
        height = float(data["height"])  # height in meters

        # Ensure valid input values
        if weight <= 0 or height <= 0:
            return jsonify({"error": "Weight and height must be positive numbers"}), 400

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Log successful calculation
        logging.info(f"BMI calculated successfully: {bmi:.2f} ({category})")

        return jsonify({
            "bmi": round(bmi, 2),
            "category": category
        }), 200

    except ValueError:
        logging.error("Invalid input received")
        return jsonify({"error": "Invalid input: weight and height must be numbers"}), 400
    except Exception as e:
        logging.error(f"Internal server error: {str(e)}")
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# ✅ Run the Flask app
if __name__ == "__main__":
    try:
        logging.info("Starting BMI API on http://127.0.0.1:5000/")
        logging.info("Available routes: %s", [rule.rule for rule in app.url_map.iter_rules()])
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        logging.error(f"Failed to start server: {str(e)}")