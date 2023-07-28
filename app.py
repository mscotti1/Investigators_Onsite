from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_session import Session
from api import api_request, insert_data, expired, parser, case_choice, stats_data, engine, check_exists
import sqlalchemy as db

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/stats")
def statistics():
    return render_template("statistics_temp.html")

##### HOMICIDE ROUTES #####
@app.route("/hom")
def homicide():
    zipcode = session.get('zipcode')
    # print("Zippy: ", zipcode)
    with engine.connect() as connection:
        stats = db.select(stats_data).filter(stats_data.c.ZipCode == zipcode)
        statistics = connection.execute(stats).fetchall()
    print(statistics[0])
    return render_template("Homicide/homicide.html", stats = statistics[0])
@app.route("/hom/file")
def hom_file():
    return render_template("Homicide/file.html")
@app.route("/hom/crime_1")
def hom_crime_1():
    return render_template("Homicide/crime_scene_1.html")
@app.route("/hom/listen_1")
def hom_listen_1():
    return render_template("Homicide/listen_1.html")
@app.route("/hom/interrogate_1")
def hom_interrogate_1():
    return render_template("Homicide/interrogate_1.html")
@app.route("/hom/court")
def hom_court_bad():
    return render_template("Homicide/court_bad.html")
@app.route("/hom/court_1")
def hom_court_1():
    return render_template("Homicide/court_1.html")
@app.route("/hom/file_2")
def hom_file_2():
    return render_template("Homicide/file_2.html")
@app.route("/hom/listen_2")
def hom_listen_2():
    return render_template("Homicide/listen_2.html")
@app.route("/hom/interrogate_2")
def hom_interrogate_2():
    return render_template("Homicide/interrogate_2.html")
@app.route("/hom/court_2")
def hom_court_2():
    return render_template("Homicide/court_2.html")
#####################################################


# MTA SLAHSER ROUTES
@app.route("/crime_scene_mta")
def crime_scene_mta():
    return render_template("MTA_Slasher/crime_scene_mta.html")

@app.route("/listen_mta")
def listen_scene_mta():
    return render_template("MTA_Slasher/listening_mta.html")

@app.route("/interrogate_mta")
def interrogate_mta():
    return render_template("MTA_Slasher/interrogation_mta.html")

@app.route("/interrogate_mta2")
def interrogate_mta_two():
    return render_template("MTA_Slasher/interrogation_mta2.html")

@app.route("/file_mta")
def file_mta():
    return render_template("MTA_Slasher/file_mta.html")

@app.route("/stats_mta")
def stats_mta():
    return render_template("MTA_Slasher/MTA_Slasher_Stats.html")
#################################################

@app.route("/listen")
def interrogation():
    return render_template("listen_temp.html")

@app.route("/interrogation")
def interactive():
    return render_template("interactive_temp.html")

@app.route("/crime_scene")
def crime_scene():
    return render_template("crime_scene_temp.html")

@app.route("/crime_scene")
def crime_scene():
    return render_template("crime_scene_temp.html")

##### CYBER ROUTES #####
@app.route("/cyber")
def Cyber_crime():
    return render_template("CyberCrime/Cyber_crime.html")
@app.route("/cyber_scene")
def cyber_crime_scene():
    return render_template("CyberCrime/crime_scene_cyber.html")
@app.route("/interr")
def cyber_interrogation():
    return render_template("CyberCrime/cyber_interrogate.html")

@app.route("/cyber_listen")
def cyber_listen():
    return render_template("CyberCrime/cyber_listen.html")
@app.route("/cyber_file")
def Cyber_file():
    return render_template("CyberCrime/cyber_file.html")
@app.route("/cyber_file2")
def Cyber_file2():
    return render_template("CyberCrime/cyber_file2.html")


##### BUG ROUTES #####
@app.route('/bug/file')
def bug_file():
    return render_template("Burglary/file.html")

@app.route('/bug/crime1')
def bug_crime_1():
    return render_template("Burglary/crime_scene_1.html")

@app.route("/bug/crime2")
def bug_crime2():
    return render_template("Burglary/crime_scene2.html")

@app.route("/bug/int")
def bug_int():
    return render_template("Burglary/interrogation.html")

@app.route("/bug/stats")
def burglary():
    return render_template("Burglary/Burglary.html")

##### OTEHR #####
@app.route("/level_select")
def level_select():
    return render_template("level_select.html")

@app.route("/file")
def file():
    return render_template("file_template.html")


@app.route("/process_zip", methods = ["POST"])
def process_zip():
    # zipcode = "11234"
    # read from a form that Maymouna sends to this route 
    # call function from api.py and pass in zipcode
    zipcode = request.form.get('zipcode')
    session['zipcode'] = zipcode
    print("Session - Zip: ", session['zipcode'])

    exists = check_exists(zipcode)
    if exists == ():
        data = api_request(zipcode)
        choice = case_choice(zipcode, data)
        row = parser(zipcode, data, choice)
        insert_data(row)

        print(zipcode)
        print("Your case is: ",choice)
    else:
        choice = exists[1]
    # switch or if else to decide which route to redirect to
    return {'key': choice}
    # pass in result from function to redirect
    # return redirect_url()

@app.route("/test_stats")
def test_stats():
    zipcode = session.get('zipcode')
    print("Zippy: ", zipcode)
    with engine.connect() as connection:
        stats = db.select(stats_data).filter(stats_data.c.ZipCode == zipcode)
        statistics = connection.execute(stats).fetchall()
    print(statistics[0])
    # statistics should always be populated with one item because that zipcode should have been inserted into the database
    return render_template("testing_stats.html", stats = statistics[0])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 8000)