from flask import Flask, render_template, request, jsonify
import random, os
import re

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_password():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request format"}), 400

        name = str(data.get("name", "")).strip()
        birthday = str(data.get("birthday", "")).strip()
        gmail = str(data.get("gmail", "")).strip()
        difficulty = str(data.get("difficulty", "medium")).strip()

        # Input validation
        errors = []
        
        if not any([name, birthday, gmail]):
            errors.append("At least one field must be provided")
        
        # Validate date format if provided
        if birthday and not re.match(r'^\d{2}/\d{2}/\d{4}$', birthday):
            errors.append("Birthday must be in dd/mm/yyyy format")
        
        # Validate email format if provided
        if gmail and "@" in gmail:
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', gmail):
                errors.append("Invalid email format")
        
        if errors:
            return jsonify({"error": "; ".join(errors)}), 400

        # Extract username from email
        gmail_user = gmail.split("@")[0] if "@" in gmail else gmail
        
        # Combine all user data
        user_data = name + birthday + gmail_user
        
        # Remove unwanted characters and keep only valid ones
        user_data = re.sub(r'[^a-zA-Z0-9@#$%&]', '', user_data)

        if not user_data:
            return jsonify({"error": "No valid characters to generate password"}), 400
        
        # Determine password length based on difficulty
        if difficulty == "easy":
            password_length = random.randint(6, 8)
        elif difficulty == "medium":
            password_length = random.randint(8, 10)
        elif difficulty == "hard":
            password_length = random.randint(10, 12)
        else:
            password_length = 8  # Default length for easy

        # Define character pools
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        special_chars = "@#$%&"

        # Ensure at least one character from each category
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_chars)
        ]

        # Fill the rest of the password length with random choices from the user data
        while len(password) < password_length:
            password.append(random.choice(user_data + special_chars))

        # Shuffle the password to ensure randomness
        random.shuffle(password)
        final_password = "".join(password)

        return jsonify({
            "password": final_password,
            "length": len(final_password),
            "source": "User provided data only"
        })

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
