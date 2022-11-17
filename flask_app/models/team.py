from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app import DATABASE   # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument



class Team:
    #these should be the same as the columns in the table
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.display_name = data["display_name"]
        self.is_owner = data['is_owner']
        self.roster = []



