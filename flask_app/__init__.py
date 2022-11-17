# __init__.py
from flask import Flask
from flask_bcrypt import Bcrypt  
app = Flask(__name__)
app.secret_key = "shhhhhh"
bcrypt = Bcrypt(app) 


DATABASE = "dtc_db"

POSITION_VALUE = {
    "QB": 3,
    "RB": 2,
    "WR": 1.5,
    "TE": 1,
    "FB": 1,
    "OT": 0,
    "DT": 0,
    "ILB": 0,
    "P": 0,
    "LB": 0,
    "FS": 0,
    "CB": 0,
    "DE": 0,
    "K": 0,
    "OLB": 0,
    "NT": 0,
    "DB": 0,
    "LS": 0,
    "SS": 0,
    "G": 0,
    "DL": 0,
    "T": 0,
    "OG": 0,
    "S": 0,
    None: 0,
}

TEAMVALS = {
    "SF": 2.5,
    "KC": 3.3,
    "BUF": 3.6,
    "NYG": 2,
    "JAX": 1.8,
    "WAS": 2.5,
    "NO": 2,
    "DEN": 2,
    "BAL": 3.4,
    "NYJ": 1.05,
    "DET": 1,
    "MIA": 1.07,
    "ATL": 1.5,
    "CLE": 1.1,
    "CAR": .9,
    "LV": 1.5,
    "CIN": 2.5,
    "HOU": 1,
    "GB": 1.1,
    "MIN": 1.15,
    "TEN": 1,
    "ARI": 1.1,
    "PHI": 1.36,
    "IND": 1.1,
    "LAR": 1.15,
    "PIT": 2.5,
    "LAC": 1.4,
    "DAL": 1.23,
    "CHI": .9,
    "NE": 1,
    "TB": 1.2,
    "SEA": 1.1,
    "OAK":0,
    None: 0
}