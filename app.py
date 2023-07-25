from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stats")
def statistics():
    return render_template("statistics_temp.html")

@app.route("/bug")
def burglary():
    return render_template("Burglary/Burglary.html")

@app.route('/bug/crime_scene_1')
def bug_crime_1():
    return render_template("Burglary/crime_scene_1.html")

@app.route("/hom")
def homicide():
    return render_template("Homicide/homicide.html")

@app.route("/hom/crime_scene_1")
def hom_crime_1():
    return render_template("Homicide/crime_scene_1.html")

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

# @app.route("/process_zip", methods = "POST")
# def process_zip():
#     pass
#     # read from a form that Maymouna sends to this route 
#     # call function from api.py and pass in zipcode
#     # switch or if else to decide which route to redirect to
#     # pass in result from function to redirect
#     # return redirect_url()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 8000)