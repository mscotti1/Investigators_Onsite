import requests
import sqlalchemy as db
from datetime import datetime, timedelta

url = 'https://zylalabs.com/api/824/crime+data+by+zipcode+api/583/get+crime+rates+by+zip'
headers = {'Authorization': 'Bearer 1723|9t0K2GR1PxMpsCefgBiK2IJBkwiBNyyCsT7KTuVi'}
# creates database if it does not already exist
engine = db.create_engine('sqlite:///stats.db')
# tracks all tables
metadata = db.MetaData()
# schema of table
# we using database as a pseudo cache
stats_data = db.Table("stats_data", metadata,
                db.Column("ZipCode", db.String(5), primary_key=True),
                db.Column("case", db.String(20)),

                db.Column("crime_overall", db.String(1)),
                db.Column("violent_grade", db.String(1)),
                db.Column("property_grade", db.String(1)),
                db.Column("other_grade", db.String(1)),
                db.Column("fact", db.String(100)),
                db.Column("risk", db.String(100)),

                db.Column("violent_rate", db.Float),
                db.Column("assault", db.Float),
                db.Column("robbery", db.Float),
                db.Column("rape", db.Float),
                db.Column("murder", db.Float),

                db.Column("property_rate", db.Float),
                db.Column("theft", db.Float),
                db.Column("vehicle", db.Float),
                db.Column("burglary", db.Float),
                db.Column("arson", db.Float),

                db.Column("other_rate", db.Float),
                db.Column("kidnapping", db.Float),
                db.Column("drug", db.Float),
                db.Column("vandalism", db.Float),
                db.Column("idenity_theft", db.Float),
                db.Column("animal_cruelty", db.Float),

                db.Column("Expiry", db.DateTime))
# creates all tables associated with metadata
# metadata.drop_all(engine)
metadata.create_all(engine)

def check_exists(zipcode):
    with engine.connect() as connection:
        # exists = db.exists(stats_data).where(stats_data.c.ZipCode == zipcode).scalar()
        query = db.select(stats_data).filter(stats_data.c.ZipCode == zipcode)
        exists = connection.execute(query).fetchall()
        if len(exists) > 0:
            print(exists[0])
            return exists[0]
        return ()

def api_request(zipcode):
    url = 'https://zylalabs.com/api/824/crime+data+by+zipcode+api/583/get+crime+rates+by+zip'
    headers = {'Authorization': 'Bearer 1723|9t0K2GR1PxMpsCefgBiK2IJBkwiBNyyCsT7KTuVi'}
    params = {'zip': zipcode}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print("data: ", data)
    return data

def parser(zipcode, data, choice):
    result = {'ZipCode': zipcode}
    result.update({'case': choice})
    expiry = datetime.now() + timedelta(days=7)
    yesterday = datetime.now() - timedelta(days = 1)
    result.update({'Expiry': expiry})

    crime_overall = data['Overall']['Overall Crime Grade']
    violent_grade = data['Overall']['Violent Crime Grade']
    property_grade = data['Overall']['Property Crime Grade']
    other_grade = data['Overall']['Other Crime Grade']
    fact = data['Overall']['Fact']
    risk = data['Overall']['Risk Detail']

    result.update([('crime_overall', crime_overall), ('violent_grade', violent_grade), ('property_grade', property_grade), 
                    ('other_grade', other_grade), ('fact', fact), ('risk', risk)])

    violent_crimes = data["Crime BreakDown"][0]["Violent Crime Rates"]
    violent_rate = data["Crime BreakDown"][0]['0']['Total Violent Crime']
    assault = violent_crimes["Assault"]
    robbery = violent_crimes["Robbery"]
    rape = violent_crimes["Rape"]
    murder = violent_crimes["Murder"]

    result.update([('violent_rate', violent_rate), ('assault', assault), 
                    ('robbery', robbery), ('rape', rape), ('murder', murder)])
    
    property_crimes = data["Crime BreakDown"][1]["Property Crime Rates"]
    property_rate = data["Crime BreakDown"][1]['0']['Total Property Crime']
    theft = property_crimes["Theft"]
    vehicle = property_crimes["Vehicle Theft"]
    burglary = property_crimes["Burglary"]
    arson = property_crimes["Arson"]

    result.update([('property_rate', property_rate), ('theft', theft), 
                    ('vehicle', vehicle), ('burglary', burglary), ('arson', arson)])
    
    other_crimes = data["Crime BreakDown"][2]["Other Crime Rates"]
    other_rate = data["Crime BreakDown"][2]['0']['Total Other Rate']
    kidnapping = other_crimes["Kidnapping"]
    drug = other_crimes["Drug Crimes"]
    vandalism = other_crimes["Vandalism"]
    idenity_theft = other_crimes["Identity Theft"]
    animal_cruelty = other_crimes["Animal Cruelty"]

    result.update([('other_rate', other_rate), ('kidnapping', kidnapping), ('drug', drug), 
                    ('vandalism', vandalism), ('idenity_theft', idenity_theft), ('animal_cruelty', animal_cruelty)])
    
    return result
# 46032
#rates are per 1000 in a standard year)

def insert_data(data):
    with engine.connect() as connection:
        connection.execute(stats_data.insert(), data)
        connection.commit()
        # return jsonify(scores)

def expired():
    with engine.connect() as connection:
        delt = db.delete(stats_data).where(stats_data.c.Expiry < datetime.now())
        connection.execute(delt)
        connection.commit()

def case_choice(zipcode, data):
    if zipcode.isnumeric() and len(zipcode)==5:
        # Process the JSON data here
        print(data["Overall"])
        print('\n')
        print(data["Crime BreakDown"])
        print('\n')
        print(data["Crime Rates Nearby"])

        violent_crimes = data["Crime BreakDown"][0]["Violent Crime Rates"]
        property_crimes = data["Crime BreakDown"][1]["Property Crime Rates"]
        other_crimes = data["Crime BreakDown"][2]["Other Crime Rates"]

        central = float(violent_crimes["Assault"]) + float(violent_crimes["Rape"]) + float(other_crimes["Kidnapping"])
        pam = float(violent_crimes["Murder"]) + float(other_crimes["Animal Cruelty"])
        roof = float(violent_crimes["Robbery"]) + float(property_crimes["Vehicle Theft"]) + float(property_crimes["Burglary"]) + float(property_crimes["Arson"]) + float(other_crimes["Vandalism"]) + float(property_crimes["Theft"])
        cyber = float(property_crimes["Theft"]) + float(other_crimes["Drug Crimes"]) + float(other_crimes["Identity Theft"])

        print("Central Tot: ", central)
        print("Pam Tot: ", pam)
        print("Roof Tot: ", roof)
        print("Cyber Tot: ", cyber)

        list = [central, pam, roof, cyber]
        choice = max(list)

        if choice == central:
            return "/central"
        elif choice == pam:
            return "/hom/file"
        elif choice == roof:
            return "/file"
        elif choice == cyber:
            return "/cyber_file"
        
    else:
        zipcode = input("please put valid zipcode: ")

# api_function("52342")
# Central: "Assault", "Rape", "Kidnapping"
# Homicide: "Murder", "Animal Cruelty"
# Roof-Man: "Burglary", "Arson", "Vehicle Theft", "Theft", "Robbery", "Vandalism"
# Cyber: "Theft", "Drug Crimes", "Identity Theft"

