# import necessary libraries
from models import create_classes
import pandas as pd
import os
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
app = Flask(__name__)

#################################################
# Database Setup
#################################################

model = joblib.load("RandomForest1.joblib")
# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"]) #probably won't use get
def send():
    if request.method == "POST":
        name = request.form["petName"]
        lat = request.form["petLat"]
        lon = request.form["petLon"]
        X_test = pd.DataFrame()
        result = model.predict(X_test)  
        return render_template("summary.html", result=result) #html needs to be called summary 
    return render_template("form.html") 

# will only end up using send route or api route

@app.route("/api/pals")
def pals():
     name = request.form["petName"]
        lat = request.form["petLat"]
        lon = request.form["petLon"]
        X_test = pd.DataFrame()
        result = model.predict(X_test)
    results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

    hover_text = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    pet_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(pet_data)


if __name__ == "__main__":
    app.run()