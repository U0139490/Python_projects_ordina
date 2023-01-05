from mysql.connector import connect, Error
from ..config import connection_detail as cd
from pathlib import Path
import json

def insert_person(name, birth_year, gender):
    """Insert a person into the Imdb databes"""
    INSERT_PERSON = """INSERT INTO persons (
                       name, birth_year, gender)
                       VALUES (%s, %s, %s)
    """
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_PERSON, (name, birth_year, gender))
                count = cursor.rowcount  # return how many rows are inserted (or updated, deleted , ...)
                connection.commit()
                return count
    except Error as err:
        print(err)
        raise


def insert_persons_from_json(filename):
    """Insert persons from json file"""

    INSERT_PERSON = """INSERT INTO persons (
                       name, birth_year, gender)
                       VALUES (%s, %s, %s)
    """
    if not Path(filename).exists():
        raise ValueError(f"File : {filename} doesn't exitst!")

    try: 
        with open(filename, 'r') as json_file:
            persons = json.load(json_file)
            data = [
                    (person['name'], int(person['birth_year']), person['gender'])
                    for person in persons
                     
            ]
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(INSERT_PERSON, data)
                count = cursor.rowcount
                connection.commit()
            return count
    except (IOError, Error) as err:
        print(err)
        raise


def delete_person_by_id(id_):
    """Delete a person from Imdb database by id"""
    DELETE_PERSON = "DELETE FROM persons WHERE id = %s"
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(DELETE_PERSON, (id_,))
                count = cursor.rowcount
                connection.commit()
                return count
    except Error as err:
        print(err)
        raise


def update_person_by_id(id_, name, birth_year, gender):
    """Update a person in Imdb database by id"""
    UPDATE_PERSON = """UPDATE persons
                       SET name=%s, birth_year=%s, gender=%s
                       WHERE id = %s
    """
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_PERSON, (name, birth_year, gender, id_))
                count = cursor.rowcount
                connection.commit()
                return count
    except Error as err:
        print(err)
        raise


def select_all_persons():
    """Select all Persons from Imdb"""
    SELECT_ALL_PERSONS = "SELECT * FROM persons"
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ALL_PERSONS)
                persons = cursor.fetchall()
                return persons
    except Error as err:
        print(err)
        raise



