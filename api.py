import requests
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
            roof = float(violent_crimes["Robbery"]) + float(property_crimes["Vehicle Theft"]) + float(property_crimes["Burglary"]) + float(property_crimes["Arson"]) + float(other_crimes["Vandalism"])
            cyber = float(property_crimes["Theft"]) + float(other_crimes["Drug Crimes"]) + float(other_crimes["Identity Theft"])

            print("Central Tot: ", central)
            print("Pam Tot: ", pam)
            print("Roof Tot: ", roof)
            print("Cyber Tot: ", cyber)

            list = [central, pam, roof, cyber]
            choice = max(list)
            print(choice)
            
        else:
            print(f"Error: {response.status_code}")

    else:
        zipcode = input("please put valid zipcode: ")

api_function("52342")
# Central: "Assault", "Rape", "Kidnapping"
# Homicide: "Murder", "Animal Cruelty"
# Roof-Man: "Burglary", "Arson", "Vehicle Theft", "Theft", "Robbery", "Vandalism"
# Cyber: "Theft", "Drug Crimes", "Identity Theft"

