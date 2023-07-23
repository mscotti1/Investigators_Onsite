from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/stats")
def statistics():
    return render_template("statistics_temp.html")

@app.route("/Bug")
def Buglary():
    return render_template("Buglary.html")

@app.route("/hom")
def homicide():
    return render_template("homicide.html")

@app.route("/Cyber")
def Cyber_crime():
    return render_template("Cyber_crime.html")

@app.route("/Central")
def Central_Park():
    return render_template("Central_Park.html")

@app.route("/listen")
def interrogation():
    return render_template("listen_temp.html")

@app.route("/interrogation")
def interactive():
    return render_template("interactive_temp.html")

@app.route("/crime_scene")
def crime_scene():
    return render_template("crime_scene_temp.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 8000)