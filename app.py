from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

# Create the data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return render_template('index.html', entries=data)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    date = data.get('date')
    weight = data.get('weight')

    if not date or not weight:
        return jsonify(success=False, message='Missing data'), 400

    new_entry = {
        'date': date,
        'weight': weight
    }

    with open(DATA_FILE, 'r') as f:
        entries = json.load(f)

    entries.append(new_entry)

    with open(DATA_FILE, 'w') as f:
        json.dump(entries, f, indent=4)

    return jsonify(success=True)

# ✅ Add this block to run the server
if __name__ == '__main__':
    app.run(debug=True)
