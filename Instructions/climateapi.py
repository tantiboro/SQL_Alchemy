from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc
import numpy as np

# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)
# Flask Setup

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# Defining Flask Routes

@app.route("/api/v1.0/precipitation")
def precipitation():
    print('precipitation status: OK')
    """Query to retrieve the last 12 month of precipitation data"""
    """Return the results from the query as a JSON representation"""
    results = session.query(Measurement.date, Measurement.prcp).\
   filter (Measurement.date >= '2016-08-23').all()
#Dictionary of query results using date as a key and precipitation as value.
    prcp_dict = []  
    for result in results:
        row = {}
        row["date"] = result[0]
        row["prcp"] = result[1]
        prcp_dict.append(row)

    return jsonify(prcp_dict)
