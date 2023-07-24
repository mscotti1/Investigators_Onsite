from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/stats")
def statistics():
    return render_template("statistics_temp.html")

@app.route("/bug")
def burglary():
    return render_template("Burglary/Burglary.html")

@app.route("/hom")
def homicide():
    return render_template("Homicide/homicide.html")

@app.route("/cyber")
def Cyber_crime():
    return render_template("CyberCrime/Cyber_crime.html")

@app.route("/central")
def Central_Park():
    return render_template("CentralPark/Central_Park.html")

@app.route("/listen")
def interrogation():
    return render_template("listen_temp.html")

@app.route("/interrogation")
def interactive():
    return render_template("interactive_temp.html")

@app.route("/crime_scene")
def crime_scene():
    return render_template("crime_scene_temp.html")

@app.route("/level_select")
def level_select():
    return render_template("level_select.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 8000)