from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/statistics")
def Statistics():
    return render_template("statistics_temp.html")

@app.route("/listen")
def interrogation():
    return render_template("listen_temp.html")

@app.route("/interrogation")
def interactive():
    return render_template("interactive_temp.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 8000)