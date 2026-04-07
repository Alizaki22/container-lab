from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)

alerts = []

@app.route('/')
def home():
    return jsonify({"status": "Container Security Monitor Running"})

@app.route('/alerts')
def get_alerts():
    return jsonify({"alerts": alerts})

@app.route('/run-attack')
def run_attack():
    alerts.append({
        "time": "now",
        "rule": "Privileged Container Started",
        "priority": "CRITICAL",
        "message": "Privileged container escape detected!"
    })
    return jsonify({"status": "Attack simulated", "alert_count": len(alerts)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
