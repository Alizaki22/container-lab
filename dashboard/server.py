from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

alerts = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/alerts')
def get_alerts():
    return jsonify({"alerts": alerts})

@app.route('/run-attack')
def run_attack():
    attacker_ip = request.remote_addr

    alerts.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "rule": "Privileged Container Started",
        "priority": "CRITICAL",
        "message": f"Unauthorized privileged container activity detected from {attacker_ip}"
    })

    return jsonify({
        "status": "Attack simulated",
        "alert_count": len(alerts)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

