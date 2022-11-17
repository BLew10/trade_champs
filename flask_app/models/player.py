from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash   
from flask_app import app, bcrypt, DATABASE, TEAMVALS, POSITION_VALUE  




class Player:
    #these should be the same as the columns in the table
    def __init__(self, data):
        self.id = data["id"]
        self.depth_chart_order = data["depth_chart_order"]
        self.position = data["position"]
        self.team = data["team"]
        self.last_name = data['last_name']
        self.first_name = data['first_name']
        self.player_id = data["player_id"]
        self.age = data['age']
        self.full_name = f"{self.first_name} {self.last_name}"
        if self.depth_chart_order == None or self.position == None or self.age == None:
            self.value = 0
        else:
            self.value = round((1/self.depth_chart_order) * 500 + (1/self.age)*100 * TEAMVALS[self.team] * POSITION_VALUE[self.position])

        

    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO players ( first_name, last_name, position, depth_chart_order, team, player_id, age, created_at , updated_at) VALUES (%(first_name)s, %(last_name)s, %(position)s, %(depth_chart_order)s, %(team)s, %(player_id)s, %(age)s, NOW(),NOW());"
        new_player_id = connectToMySQL(DATABASE).query_db(query, data)
        return new_player_id
    

    @classmethod
    def get_all(cls):
        query_rb = "SELECT * FROM players WHERE position = 'RB';"
        query_te = "SELECT * FROM players WHERE position = 'TE';"
        query_qb = "SELECT * FROM players WHERE position = 'QB';"
        query_wr = "SELECT * FROM players WHERE position = 'WR';"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        #returns a list of dicts
        list_of_rb_dicts_from_db = connectToMySQL(DATABASE).query_db(query_rb)
        list_of_te_dicts_from_db = connectToMySQL(DATABASE).query_db(query_te)
        list_of_qb_dicts_from_db = connectToMySQL(DATABASE).query_db(query_qb)
        list_of_wr_dicts_from_db = connectToMySQL(DATABASE).query_db(query_wr)
        list_of_players_dicts_from_db = [*list_of_rb_dicts_from_db,*list_of_te_dicts_from_db,*list_of_qb_dicts_from_db,*list_of_wr_dicts_from_db ]
        if not list_of_players_dicts_from_db:
            return False
        # Create an empty list to append our instances of friends
        list_of_players_instances = []
        # Iterate over the db results and create instances of friends with cls.
        for player_dict in list_of_players_dicts_from_db:
            list_of_players_instances.append(cls(player_dict))
        return list_of_players_instances

    @classmethod
    def get_one(cls, data:dict):
        query = 'SELECT * FROM players WHERE player_id = %(player_id)s;'
        list_of_one_player_dict = connectToMySQL(DATABASE).query_db(query, data)
        if not list_of_one_player_dict:
            return False
        return cls(list_of_one_player_dict[0])

    @classmethod
    def delete_player(cls, data:dict):
        query = 'DELETE FROM players WHERE id = %(id)s;'
        player = connectToMySQL(DATABASE).query_db(query, data)
        return player

    @classmethod
    def update_player(cls, data:dict):
        query = 'UPDATE players SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;'
        player = connectToMySQL(DATABASE).query_db(query, data)
        return cls(player)

