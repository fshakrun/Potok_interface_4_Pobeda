from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ego18/billing/api/pending_counts")
def pending_counts():
    return jsonify({
        "all_count": 5
    })


@app.route("/ego18/billing/api/filter_counts")
def filter_counts():
    return jsonify({
        "comments": 3,
        "reviews": 2
    })


@app.route("/ego18/cloner/stop/clone_18/bot")
def stop_bot():
    return jsonify({
        "success": True
    })


@app.route("/ego18/cloner/start/clone_18/bot")
def start_bot():
    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
