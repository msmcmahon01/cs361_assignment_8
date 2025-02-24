from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define your adjective lists
adjective_lists = [
    "Poke",
    "Great",
    "Ultra",
    "Master",
    "Super",
    "Hyper",
    "Max"
]

# Endpoint to add an adjective to an item
@app.route('/addAdjective', methods=['POST'])
def add_adjective():
    data = request.json
    item_name = data.get('itemName')

    adjective = random.choice(adjective_lists)
    modified_name = f"{adjective} {item_name}"

    return jsonify({"modifiedName": modified_name})

# Error handling for invalid requests
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request"}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
