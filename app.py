# import necessary libraries
# from models import create_classes
import pandas as pd
import joblib
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#################################################
# Database Setup
#################################################

model = joblib.load("RandomForest2.joblib")
@app.route("/")
def home():
    return render_template("form2.html")


@app.route("/send", methods=["GET", "POST"]) #probably won't use get
def send():
    if request.method == "POST":
        neighborhood = request.form["neighborhood"]
        building_type = request.form["BuildingType"]
        zip1 = request.form["ZipCode"] # changed to zip1 because zip is a keyword in Python and should not be used as var name
        units = request.form["totalUnits"]
        sqft = request.form["sqft"]
        year = request.form["year"]
        # X_test = pd.read_csv("x_test.csv")
        # result = model.predict(X_test)  
        # return render_template("summary.html", result=result) #html needs to be called summary 

        # Start of Claudia changes

        # Make sqft input numeric based on binning options
        if "-" in sqft:
            sqft1 = int(sqft.split("-")[0]) + 500
        else:
            sqft1 = 51000

        # Convert set of inputs into a dictionary (and then dataframe)
        dic = {"ZIP CODE": int(zip1),
                "TOTAL UNITS": int(units),
                "SQFT": sqft1,
                "YEAR BUILT": int(year)}

        # list of all model params
        model_params = ['ZIP CODE', 'TOTAL UNITS', 'SQFT', 'YEAR BUILT', 'NEIGHBORHOOD_ALPHABET CITY', 'NEIGHBORHOOD_ANNADALE', 'NEIGHBORHOOD_ARDEN HEIGHTS', 'NEIGHBORHOOD_ARROCHAR', 'NEIGHBORHOOD_ARROCHAR-SHORE ACRES', 'NEIGHBORHOOD_ARVERNE', 'NEIGHBORHOOD_ASTORIA', 'NEIGHBORHOOD_BATH BEACH', 'NEIGHBORHOOD_BATHGATE', 'NEIGHBORHOOD_BAY RIDGE', 'NEIGHBORHOOD_BAYCHESTER', 'NEIGHBORHOOD_BAYSIDE', 'NEIGHBORHOOD_BEDFORD PARK/NORWOOD', 'NEIGHBORHOOD_BEDFORD STUYVESANT', 'NEIGHBORHOOD_BEECHHURST', 'NEIGHBORHOOD_BELLE HARBOR', 'NEIGHBORHOOD_BELLEROSE', 'NEIGHBORHOOD_BELMONT', 'NEIGHBORHOOD_BENSONHURST', 'NEIGHBORHOOD_BERGEN BEACH', 'NEIGHBORHOOD_BOERUM HILL', 'NEIGHBORHOOD_BOROUGH PARK', 'NEIGHBORHOOD_BRIARWOOD', 'NEIGHBORHOOD_BRIGHTON BEACH', 'NEIGHBORHOOD_BROAD CHANNEL', 'NEIGHBORHOOD_BRONX PARK', 'NEIGHBORHOOD_BRONXDALE', 'NEIGHBORHOOD_BROOKLYN HEIGHTS', 'NEIGHBORHOOD_BROWNSVILLE', 'NEIGHBORHOOD_BULLS HEAD', 'NEIGHBORHOOD_BUSH TERMINAL', 'NEIGHBORHOOD_BUSHWICK', 'NEIGHBORHOOD_CAMBRIA HEIGHTS', 'NEIGHBORHOOD_CANARSIE', 'NEIGHBORHOOD_CARROLL GARDENS', 'NEIGHBORHOOD_CASTLE HILL/UNIONPORT', 'NEIGHBORHOOD_CASTLETON CORNERS', 'NEIGHBORHOOD_CHELSEA', 'NEIGHBORHOOD_CHINATOWN', 'NEIGHBORHOOD_CITY ISLAND', 'NEIGHBORHOOD_CITY ISLAND-PELHAM STRIP', 'NEIGHBORHOOD_CIVIC CENTER', 'NEIGHBORHOOD_CLINTON', 'NEIGHBORHOOD_CLINTON HILL', 'NEIGHBORHOOD_CLOVE LAKES', 'NEIGHBORHOOD_CO-OP CITY', 'NEIGHBORHOOD_COBBLE HILL', 'NEIGHBORHOOD_COBBLE HILL-WEST', 'NEIGHBORHOOD_COLLEGE POINT', 'NEIGHBORHOOD_CONCORD', 'NEIGHBORHOOD_CONCORD-FOX HILLS', 'NEIGHBORHOOD_CONEY ISLAND', 'NEIGHBORHOOD_CORONA', 'NEIGHBORHOOD_COUNTRY CLUB', 'NEIGHBORHOOD_CROTONA PARK', 'NEIGHBORHOOD_CROWN HEIGHTS', 'NEIGHBORHOOD_CYPRESS HILLS', 'NEIGHBORHOOD_DONGAN HILLS', 'NEIGHBORHOOD_DONGAN HILLS-COLONY', 'NEIGHBORHOOD_DONGAN HILLS-OLD TOWN', 'NEIGHBORHOOD_DOUGLASTON', 'NEIGHBORHOOD_DOWNTOWN-FULTON FERRY', 'NEIGHBORHOOD_DOWNTOWN-FULTON MALL', 'NEIGHBORHOOD_DOWNTOWN-METROTECH', 'NEIGHBORHOOD_DYKER HEIGHTS', 'NEIGHBORHOOD_EAST ELMHURST', 'NEIGHBORHOOD_EAST NEW YORK', 'NEIGHBORHOOD_EAST TREMONT', 'NEIGHBORHOOD_EAST VILLAGE', 'NEIGHBORHOOD_ELMHURST', 'NEIGHBORHOOD_ELTINGVILLE', 'NEIGHBORHOOD_EMERSON HILL', 'NEIGHBORHOOD_FAR ROCKAWAY', 'NEIGHBORHOOD_FASHION', 'NEIGHBORHOOD_FIELDSTON', 'NEIGHBORHOOD_FINANCIAL', 'NEIGHBORHOOD_FLATBUSH-CENTRAL', 'NEIGHBORHOOD_FLATBUSH-EAST', 'NEIGHBORHOOD_FLATBUSH-LEFFERTS GARDEN', 'NEIGHBORHOOD_FLATBUSH-NORTH', 'NEIGHBORHOOD_FLATIRON', 'NEIGHBORHOOD_FLATLANDS', 'NEIGHBORHOOD_FLORAL PARK', 'NEIGHBORHOOD_FLUSHING-NORTH', 'NEIGHBORHOOD_FLUSHING-SOUTH', 'NEIGHBORHOOD_FORDHAM', 'NEIGHBORHOOD_FOREST HILLS', 'NEIGHBORHOOD_FORT GREENE', 'NEIGHBORHOOD_FRESH KILLS', 'NEIGHBORHOOD_FRESH MEADOWS', 'NEIGHBORHOOD_GERRITSEN BEACH', 'NEIGHBORHOOD_GLEN OAKS', 'NEIGHBORHOOD_GLENDALE', 'NEIGHBORHOOD_GOWANUS', 'NEIGHBORHOOD_GRAMERCY', 'NEIGHBORHOOD_GRANT CITY', 'NEIGHBORHOOD_GRASMERE', 'NEIGHBORHOOD_GRAVESEND', 'NEIGHBORHOOD_GREAT KILLS', 'NEIGHBORHOOD_GREAT KILLS-BAY TERRACE', 'NEIGHBORHOOD_GREENPOINT', 'NEIGHBORHOOD_GREENWICH VILLAGE-CENTRAL', 'NEIGHBORHOOD_GREENWICH VILLAGE-WEST', 'NEIGHBORHOOD_GRYMES HILL', 'NEIGHBORHOOD_HAMMELS', 'NEIGHBORHOOD_HARLEM-CENTRAL', 'NEIGHBORHOOD_HARLEM-EAST', 'NEIGHBORHOOD_HARLEM-UPPER', 'NEIGHBORHOOD_HARLEM-WEST', 'NEIGHBORHOOD_HIGHBRIDGE/MORRIS HEIGHTS', 'NEIGHBORHOOD_HILLCREST', 'NEIGHBORHOOD_HOLLIS', 'NEIGHBORHOOD_HOLLIS HILLS', 'NEIGHBORHOOD_HOLLISWOOD', 'NEIGHBORHOOD_HOWARD BEACH', 'NEIGHBORHOOD_HUGUENOT', 'NEIGHBORHOOD_HUNTS POINT', 'NEIGHBORHOOD_INWOOD', 'NEIGHBORHOOD_JACKSON HEIGHTS', 'NEIGHBORHOOD_JAMAICA', 'NEIGHBORHOOD_JAMAICA BAY', 'NEIGHBORHOOD_JAMAICA ESTATES', 'NEIGHBORHOOD_JAMAICA HILLS', 'NEIGHBORHOOD_JAVITS CENTER', 'NEIGHBORHOOD_KENSINGTON', 'NEIGHBORHOOD_KEW GARDENS', 'NEIGHBORHOOD_KINGSBRIDGE HTS/UNIV HTS', 'NEIGHBORHOOD_KINGSBRIDGE/JEROME PARK', 'NEIGHBORHOOD_KIPS BAY', 'NEIGHBORHOOD_LAURELTON', 'NEIGHBORHOOD_LITTLE ITALY', 'NEIGHBORHOOD_LITTLE NECK', 'NEIGHBORHOOD_LIVINGSTON', 'NEIGHBORHOOD_LONG ISLAND CITY', 'NEIGHBORHOOD_LOWER EAST SIDE', 'NEIGHBORHOOD_MADISON', 'NEIGHBORHOOD_MANHATTAN BEACH', 'NEIGHBORHOOD_MANHATTAN VALLEY', 'NEIGHBORHOOD_MANOR HEIGHTS', 'NEIGHBORHOOD_MARINE PARK', 'NEIGHBORHOOD_MARINERS HARBOR', 'NEIGHBORHOOD_MASPETH', 'NEIGHBORHOOD_MELROSE/CONCOURSE', 'NEIGHBORHOOD_MIDDLE VILLAGE', 'NEIGHBORHOOD_MIDLAND BEACH', 'NEIGHBORHOOD_MIDTOWN EAST', 'NEIGHBORHOOD_MIDTOWN WEST', 'NEIGHBORHOOD_MIDWOOD', 'NEIGHBORHOOD_MILL BASIN', 'NEIGHBORHOOD_MORRIS PARK/VAN NEST', 'NEIGHBORHOOD_MORRISANIA/LONGWOOD', 'NEIGHBORHOOD_MOTT HAVEN/PORT MORRIS', 'NEIGHBORHOOD_MOUNT HOPE/MOUNT EDEN', 'NEIGHBORHOOD_MURRAY HILL', 'NEIGHBORHOOD_NAVY YARD', 'NEIGHBORHOOD_NEPONSIT', 'NEIGHBORHOOD_NEW BRIGHTON', 'NEIGHBORHOOD_NEW BRIGHTON-ST. GEORGE', 'NEIGHBORHOOD_NEW DORP', 'NEIGHBORHOOD_NEW DORP-BEACH', 'NEIGHBORHOOD_NEW DORP-HEIGHTS', 'NEIGHBORHOOD_NEW SPRINGVILLE', 'NEIGHBORHOOD_OAKLAND GARDENS', 'NEIGHBORHOOD_OAKWOOD', 'NEIGHBORHOOD_OAKWOOD-BEACH', 'NEIGHBORHOOD_OCEAN HILL', 'NEIGHBORHOOD_OCEAN PARKWAY-NORTH', 'NEIGHBORHOOD_OCEAN PARKWAY-SOUTH', 'NEIGHBORHOOD_OLD MILL BASIN', 'NEIGHBORHOOD_OZONE PARK', 'NEIGHBORHOOD_PARK SLOPE', 'NEIGHBORHOOD_PARK SLOPE SOUTH', 'NEIGHBORHOOD_PARKCHESTER', 'NEIGHBORHOOD_PELHAM GARDENS', 'NEIGHBORHOOD_PELHAM PARKWAY NORTH', 'NEIGHBORHOOD_PELHAM PARKWAY SOUTH', 'NEIGHBORHOOD_PLEASANT PLAINS', 'NEIGHBORHOOD_PORT IVORY', 'NEIGHBORHOOD_PORT RICHMOND', 'NEIGHBORHOOD_PRINCES BAY', 'NEIGHBORHOOD_PROSPECT HEIGHTS', 'NEIGHBORHOOD_QUEENS VILLAGE', 'NEIGHBORHOOD_RED HOOK', 'NEIGHBORHOOD_REGO PARK', 'NEIGHBORHOOD_RICHMOND HILL', 'NEIGHBORHOOD_RICHMONDTOWN', 'NEIGHBORHOOD_RICHMONDTOWN-LIGHTHS HILL', 'NEIGHBORHOOD_RIDGEWOOD', 'NEIGHBORHOOD_RIVERDALE', 'NEIGHBORHOOD_ROCKAWAY PARK', 'NEIGHBORHOOD_ROOSEVELT ISLAND', 'NEIGHBORHOOD_ROSEBANK', 'NEIGHBORHOOD_ROSEDALE', 'NEIGHBORHOOD_ROSSVILLE', 'NEIGHBORHOOD_ROSSVILLE-CHARLESTON', 'NEIGHBORHOOD_ROSSVILLE-RICHMOND VALLEY', 'NEIGHBORHOOD_SCHUYLERVILLE/PELHAM BAY', 'NEIGHBORHOOD_SEAGATE', 'NEIGHBORHOOD_SHEEPSHEAD BAY', 'NEIGHBORHOOD_SILVER LAKE', 'NEIGHBORHOOD_SO. JAMAICA-BAISLEY PARK', 'NEIGHBORHOOD_SOHO', 'NEIGHBORHOOD_SOUNDVIEW', 'NEIGHBORHOOD_SOUTH BEACH', 'NEIGHBORHOOD_SOUTH JAMAICA', 'NEIGHBORHOOD_SOUTH OZONE PARK', 'NEIGHBORHOOD_SOUTHBRIDGE', 'NEIGHBORHOOD_SPRING CREEK', 'NEIGHBORHOOD_SPRINGFIELD GARDENS', 'NEIGHBORHOOD_ST. ALBANS', 'NEIGHBORHOOD_STAPLETON', 'NEIGHBORHOOD_STAPLETON-CLIFTON', 'NEIGHBORHOOD_SUNNYSIDE', 'NEIGHBORHOOD_SUNSET PARK', 'NEIGHBORHOOD_THROGS NECK', 'NEIGHBORHOOD_TODT HILL', 'NEIGHBORHOOD_TOMPKINSVILLE', 'NEIGHBORHOOD_TOTTENVILLE', 'NEIGHBORHOOD_TRAVIS', 'NEIGHBORHOOD_TRIBECA', 'NEIGHBORHOOD_UPPER EAST SIDE (59-79)', 'NEIGHBORHOOD_UPPER EAST SIDE (79-96)', 'NEIGHBORHOOD_UPPER EAST SIDE (96-110)', 'NEIGHBORHOOD_UPPER WEST SIDE (59-79)', 'NEIGHBORHOOD_UPPER WEST SIDE (79-96)', 'NEIGHBORHOOD_UPPER WEST SIDE (96-116)', 'NEIGHBORHOOD_VAN CORTLANDT PARK', 'NEIGHBORHOOD_WAKEFIELD', 'NEIGHBORHOOD_WASHINGTON HEIGHTS LOWER', 'NEIGHBORHOOD_WASHINGTON HEIGHTS UPPER', 'NEIGHBORHOOD_WEST NEW BRIGHTON', 'NEIGHBORHOOD_WESTCHESTER', 'NEIGHBORHOOD_WESTERLEIGH', 'NEIGHBORHOOD_WHITESTONE', 'NEIGHBORHOOD_WILLIAMSBRIDGE', 'NEIGHBORHOOD_WILLIAMSBURG-CENTRAL', 'NEIGHBORHOOD_WILLIAMSBURG-EAST', 'NEIGHBORHOOD_WILLIAMSBURG-NORTH', 'NEIGHBORHOOD_WILLIAMSBURG-SOUTH', 'NEIGHBORHOOD_WILLOWBROOK', 'NEIGHBORHOOD_WINDSOR TERRACE', 'NEIGHBORHOOD_WOODHAVEN', 'NEIGHBORHOOD_WOODLAWN', 'NEIGHBORHOOD_WOODROW', 'NEIGHBORHOOD_WOODSIDE', 'NEIGHBORHOOD_WYCKOFF HEIGHTS', 'BUILDING CLASS CATEGORY_02 TWO FAMILY DWELLINGS                    ', 'BUILDING CLASS CATEGORY_03 THREE FAMILY DWELLINGS                  ', 'BUILDING CLASS CATEGORY_07 RENTALS - WALKUP APARTMENTS             ', 'BUILDING CLASS CATEGORY_08 RENTALS - ELEVATOR APARTMENTS           ', 'BUILDING CLASS CATEGORY_09 COOPS - WALKUP APARTMENTS               ', 'BUILDING CLASS CATEGORY_10 COOPS - ELEVATOR APARTMENTS             ', 'BUILDING CLASS CATEGORY_11A CONDO-RENTALS                           ', 'BUILDING CLASS CATEGORY_12 CONDOS - WALKUP APARTMENTS              ', 'BUILDING CLASS CATEGORY_13 CONDOS - ELEVATOR APARTMENTS            ', 'BUILDING CLASS CATEGORY_14 RENTALS - 4-10 UNIT                     ', 'BUILDING CLASS CATEGORY_15 CONDOS - 2-10 UNIT RESIDENTIAL          ', 'BUILDING CLASS CATEGORY_16 CONDOS - 2-10 UNIT WITH COMMERCIAL UNIT ', 'BUILDING CLASS CATEGORY_17 CONDO COOPS                             ', 'BUILDING CLASS CATEGORY_46 CONDO STORE BUILDINGS                   ']
        # Add dummies to dic
        for m in model_params:
            if "NEIGHBORHOOD" in m:
                if neighborhood in m:
                    dic[m] = 1
                else:
                    dic[m] = 0
            if "BUILDING CLASS" in m:
                if building_type in m:
                    dic[m] = 1
                else:
                    dic[m] = 0
        
        # convert to df
        inputdf = pd.DataFrame([dic])


        result = (model.predict(inputdf))[0]  
        #tohtml = [dic, result]
        #tohtml = {"dic": dic, "results": result}
        #return render_template('summary.html', info=result[0])
        # End of Claudia changes



        return (f'The Price Prediction is: ${result:.2f}')
    # X_test = pd.read_csv("x_test.csv")
    # result = model.predict(X_test)  
    # return (f'{result}')

# will only end up using send route or api route

# @app.route("/api/pals")
# def pals():
#      name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]
#         X_test = pd.DataFrame()
#         result = model.predict(X_test)
#     results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]

#     pet_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",
#         "lat": lat,
#         "lon": lon,
#         "text": hover_text,
#         "hoverinfo": "text",
#         "marker": {
#             "size": 50,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

#     return jsonify(pet_data)


if __name__ == "__main__":
    app.run()