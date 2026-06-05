from flask import Flask, jsonify

from services import get_depots, get_vehicles
from knapsack import get_optimal_tasks

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Vehicle Scheduler Running"
    })


@app.route("/schedule")
def schedule():
    depots_data = get_depots()
    vehicles_data = get_vehicles()

    depots = depots_data.get("depots", [])
    vehicles = vehicles_data.get("vehicles", [])

    result = []

    for depot in depots:
        capacity = depot["MechanicHours"]

        optimal = get_optimal_tasks(
            vehicles,
            capacity
        )

        result.append({
            "DepotID": depot["ID"],
            "MechanicHours": capacity,
            "MaximumImpact": optimal["maxImpact"],
            "SelectedTasks": optimal["selectedTasks"]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )