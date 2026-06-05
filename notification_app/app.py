from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

notifications = []


@app.route("/")
def home():
    return jsonify({
        "message": "Notification Service Running"
    })


@app.route("/notifications", methods=["POST"])
def send_notification():
    data = request.json

    notification = {
        "id": len(notifications) + 1,
        "user": data.get("user"),
        "channel": data.get("channel"),
        "message": data.get("message"),
        "status": "SENT",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    notifications.append(notification)

    return jsonify(notification), 201


@app.route("/notifications", methods=["GET"])
def get_notifications():
    return jsonify(notifications)


@app.route("/notifications/<int:notification_id>", methods=["GET"])
def get_notification(notification_id):
    for notification in notifications:
        if notification["id"] == notification_id:
            return jsonify(notification)

    return jsonify({"error": "Notification not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")