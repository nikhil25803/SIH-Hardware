from flask import Flask, request
import requests
import math, re
import json
from datetime import datetime

app = Flask(__name__)


@app.route("/test")
def index():
    response = {"data": "Hello World"}

    return json.loads(json.dumps(response, default=str))


@app.route("/getSensorData", methods=["GET"])
def send_command():
    try:
        data = requests.get("http://192.168.1.15/getSensorData").text
        res_list = re.split(r"\n", data)

        # Reading resistance and led_status
        resistance = int(res_list[0])
        led_status = int(res_list[1])

        power = (1.25 * math.pow(10, 7)) * math.pow(int(resistance), -1.4059)

        response = {
            "status": "success",
            "led_status": led_status,
            "resistance": int(resistance),
            "power": power,
            "timestamp": datetime.now().time(),
        }

    except:
        response = {
            "status": "fail",
            "led_status": "fail",
            "resistance": 0,
            "power": 0,
            "timestamp": datetime.now().time(),
        }
    return json.loads(json.dumps(response, default=str))


@app.route("/setState", methods=["GET"])
def set_state():
    request_state = request.args.get("state")

    if request_state not in ["turnOn", "turnOff"]:
        return json.dumps(json.loads({"message": "Invalid Request"}))

    try:
        make_request = requests.get(f"http://192.168.1.15/{request_state}")
        response = {
            "request": request_state,
            "status": make_request.status_code,
            "message": "State changed successfully.",
        }
    except:
        response = {
            "request": request_state,
            "status": make_request.status_code,
            "message": "Unable to make request",
        }
    return json.loads(json.dumps(response, default=str))


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
