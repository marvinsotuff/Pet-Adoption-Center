import sqlite3
from db import DB

class Pet:
    def __init__(self, id, name, species, age, shelter_id):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.shelter_id = shelter_id

    #---------ORM Methods---------
    @classmethod
    def create(cls, name, species, age, shelter_id):
        query = "INSERT INTO pets (name, species, age, shelter_id) VALUES (?, ?, ?, ?)"
        DB.execute(query, (name, species, age, shelter_id))
        print(f"Pet '{name}' created.")

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pets"
        return DB.execute(query).fetchall()
        return rows

    @classmethod
    def find_by_id(cls, pet_id):
        query = "SELECT * FROM pets WHERE id = ?"
        row = DB.execute(query, (pet_id,)).fetchone()
        return row

    @classmethod
    def delete(cls, pet_id):
        query = "DELETE FROM pets WHERE id = ?"
        DB.execute(query, (pet_id,))
        print(f"Pet with ID {pet_id} deleted.")

    @classmethod
    def find_by_shelter(cls, shelter_id):
        query = "SELECT * FROM pets WHERE shelter_id = ?"
        return DB.execute(query, (shelter_id,)).fetchall()
        return rows