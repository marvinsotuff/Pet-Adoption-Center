import sqlite3
from db import DB

class Shelter:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    #---------ORM Methods---------
    @classmethod
    def create(cls, name, location):
        query = "INSERT INTO shelters (name, location) VALUES (?, ?)"
        DB.execute(query, (name, location))
        print(f"Shelter '{name}' created.")

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shelters"
        return DB.execute(query).fetchall()
        return rows
    
    @classmethod
    def find_by_id(cls, shelter_id):
        query = "SELECT * FROM shelters WHERE id = ?"
        return DB.execute(query, (shelter_id,)).fetchone()
        return row
    
    @classmethod
    def delete(cls, shelter_id):
        query = "DELETE FROM shelters WHERE id = ?"
        DB.execute(query, (shelter_id,))
        print(f"Shelter with ID {shelter_id} deleted.")

    