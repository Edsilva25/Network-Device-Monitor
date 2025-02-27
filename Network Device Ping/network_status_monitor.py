import subprocess
import json
from flask import Flask, jsonify

# List of network devices
devices = [
    "8.8.8.8",  # Google DNS
    "1.1.1.1",  # Cloudflare DNS
    "example.com"
]


def ping_device(host):
    try:
        result = subprocess.run(["ping", "-n", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Pinging {host}...\n{result.stdout}") 
        return result.returncode == 0  
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return False


def check_devices():
    status_log = {}
    for device in devices:
        status = "Online" if ping_device(device) else "Offline"
        status_log[device] = status
    
    with open("status_log.json", "w") as file:
        json.dump(status_log, file, indent=4)
    
    return status_log


app = Flask(__name__)

@app.route("/status", methods=["GET"])
def get_status():
    try:
        with open("status_log.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No status log found"}), 404

@app.route("/check", methods=["POST"])
def manual_check():
    status = check_devices()
    return jsonify(status)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
