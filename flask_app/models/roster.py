from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import  DATABASE   


class Roster:
    def __init__(self, data):
        self.players = data["players"]
        self.owner_id = data["owner_id"]
        self.league_id = data["league_id"]
        self.roster_id = data["roster_id"]


