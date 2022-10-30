import os
from flask_app.config.mysqlconnection import connectToMySQL

class User: 

    modelo = 'users' #nombre de tabla

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.modelo};"
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query)
        users = []

        for usuarios in results:
            users.append( cls(usuarios) )
        return users
    @classmethod
    def save(cls, data ):
        query = f"INSERT INTO {cls.modelo} ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data )     
