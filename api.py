import requests
import sqlalchemy as db

# creates database if it does not already exist
engine = db.create_engine('sqlite:///stats.db')
# tracks all tables
metadata = db.MetaData()
# schema of table
# we using database as a pseudo cache
stats_data = db.Table("stats_data", metadata,
                db.Column("ZipCode", db.String(5)),

                db.Column("Overall Crime Grade", db.Float),
                db.Column("Violent Crime Grade", db.Float),
                db.Column("Property Crime Grade", db.Float),
                db.Column("Other Crime Grade", db.Float),
                db.Column("Fact", db.Float),
                db.Column("Risk Detail", db.Float),

                db.Column("Total Violent Crime Rate", db.Float),
                db.Column("Assault Crime Rate", db.Float),
                db.Column("Robbery Crime Rate", db.Float),
                db.Column("Rape Crime Rate", db.Float),
                db.Column("Murder Crime Rate", db.Float),

                db.Column("Total Property Crime Rate", db.Float),
                db.Column("Theft Crime Rate", db.Float),
                db.Column("Vehicle Theft Crime Rate", db.Float),
                db.Column("Burglary Crime Rate", db.Float),
                db.Column("Arson Crime Rate", db.Float),

                db.Column("Total Other Crime Rate", db.Float),
                db.Column("Kidnapping Crime Rate", db.Float),
                db.Column("Drug Crime Rate", db.Float),
                db.Column("Vandalism Crime Rate", db.Float),
                db.Column("Identity Theft Crime Rate", db.Float),
                db.Column("Animal Cruelty Crime Rate", db.Float),

                db.Column("Expiry Time", db.DateTime))
# creates all tables associated with metadata
metadata.create_all(engine)

url = 'https://zylalabs.com/api/824/crime+data+by+zipcode+api/583/get+crime+rates+by+zip'
headers = {'Authorization': 'Bearer 1723|9t0K2GR1PxMpsCefgBiK2IJBkwiBNyyCsT7KTuVi'}
# zipcode = input("practice: ")

def api_function(zipcode):
    if zipcode.isnumeric() and len(zipcode)==5:
        params = {'zip': zipcode}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
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
                return "central"
            elif choice == pam:
                return "homicide"
            elif choice == roof:
                return "burglary"
            elif choice == cyber:
                return "cyber"
            
        else:
            print(f"Error: {response.status_code}")

    else:
        zipcode = input("please put valid zipcode: ")

# api_function("52342")
# Central: "Assault", "Rape", "Kidnapping"
# Homicide: "Murder", "Animal Cruelty"
# Roof-Man: "Burglary", "Arson", "Vehicle Theft", "Theft", "Robbery", "Vandalism"
# Cyber: "Theft", "Drug Crimes", "Identity Theft"

