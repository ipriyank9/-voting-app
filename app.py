from flask import Flask, jsonify

app = Flask(__name__)

votes = {}


@app.route("/")
def home():
    return "Welcome to the App"


@app.route("/health")
def health():
    return "App is running"


@app.route("/vote/<name>")
def vote(name):
    votes[name] = votes.get(name, 0) + 1
    return f"Vote recorded for {name}"


@app.route("/results")
def results():
    return jsonify(votes)


if __name__ == "__main__":
    app.run(debug=True)