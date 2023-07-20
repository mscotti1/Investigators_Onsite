from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/Statistics")
def Statistics():
    return render_template("Statistics.html")

@app.route("/interrogation")
def interrogation():
    return render_template("interrogation_temp.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 8000)