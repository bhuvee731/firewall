from flask import Flask, render_template, request, jsonify
import time
import re

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Firmware scan route
@app.route('/scan', methods=['POST'])
def scan_firmware():
    ip = request.form.get('device_ip', '')

    # Basic validation of IP address
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if not re.match(ip_pattern, ip):
        return jsonify({
            "status": "error",
            "message": "Invalid IP address format."
        }), 400

    # Simulate a scan delay
    time.sleep(2)

    # Simulated scan result (this would be replaced with actual logic)
    outdated_firmwares = ["192.168.1.100", "192.168.1.105"]  # Dummy IPs with outdated firmware

    if ip in outdated_firmwares:
        message = f"Warning: Outdated firmware detected on device {ip}."
    else:
        message = f"Firmware is up-to-date on device {ip}."

    return jsonify({
        "status": "success",
        "message": message
    })

if __name__ == '__main__':
app.run(debug=True)
