from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app, bcrypt, DATABASE   # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument
#regex 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

#not in use yet

class User:
    # these should be the same as the columns in the table
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , password , created_at , updated_at ) VALUES (%(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );"
        new_user_id = connectToMySQL(DATABASE).query_db(query, data)
        return new_user_id

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        list_of_one_user_dict = connectToMySQL(DATABASE).query_db(query, data)
        if not list_of_one_user_dict:
            return False
        return cls(list_of_one_user_dict[0])

    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        user = connectToMySQL(DATABASE).query_db(query, data)
        return user

    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;'
        user = connectToMySQL(DATABASE).query_db(query, data)
        return cls(user)

    # IF EMAIL FOR USERS
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        # returns a list of dicts
        list_dict_user_email = connectToMySQL(
            DATABASE).query_db(query, data)
        # Didn't find a matching user
        if len(list_dict_user_email) < 1:
            return False
        return cls(list_dict_user_email[0])

    @staticmethod
    def validate_user(user):
        is_valid = True  # we assume this is true

        if len(user['first_name']) < 1:
            flash("Must input first name.", "registration")
            is_valid = False

        if len(user['last_name']) < 1:
            flash("Must input last name.", "registration")
            is_valid = False

        if len(user['password']) < 1:
            flash("Passwords needs to be longer than 1 characters", "registration")
            is_valid = False

        if user['password'] != user['confirm_password']:
            flash("Passwords do not match", "registration")         
            is_valid = False
        # test whether a field matches the pattern, email check for users
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", "registration")
            is_valid = False

        return is_valid
