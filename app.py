from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to send requests

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/yogapathy"  
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('contact.html')  # Ensure contact.html is in "templates" folder

# ✅ Contact Form Route to Receive Data
@app.route('/contact', methods=['POST'])
def contact():
    data = request.json  # Receive JSON data from frontend
    if data:
        mongo.db.contacts.insert_one(data)  # Insert into MongoDB
        return jsonify({"message": "Contact details submitted successfully!"}), 201
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
