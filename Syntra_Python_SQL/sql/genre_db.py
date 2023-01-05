from mysql.connector import connect, Error
from ..config import connection_detail as cd
from pathlib import Path
import json

def insert_genre(name):
    """Insert a genre into the Imdb databes"""
    INSERT_GENRE = """INSERT INTO genres (
                      name)
                      VALUES (%s)
    """
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_GENRE, (name,))
                count = cursor.rowcount  
                connection.commit()
        return count
    except Error as err:
        print(err)
        raise


def insert_genres_from_json(filename):
    """Insert persons from json file"""

    INSERT_GENRE = """INSERT INTO genres (
                      name)
                      VALUES (%s)
    """
    if not Path(filename).exists():
        raise ValueError(f"File : {filename} doesn't exist!")

    try: 
        with open(filename, 'r') as json_file:
            genres = json.load(json_file)
            data = [(genre['name'],) for genre in genres]

        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(INSERT_GENRE, data)
                count = cursor.rowcount
                connection.commit()
        return count
    except (IOError, Error) as err:
        print(err)
        raise


def delete_genre_by_id(id_):
    """Delete a genre from Imdb database by id"""
    DELETE_GENRE = "DELETE FROM genres WHERE id = %s"
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(DELETE_GENRE, (id_,))
                count = cursor.rowcount
                connection.commit()
        return count
    except Error as err:
        print(err)
        raise


def update_genre_by_id(id_, name):
    """Update a genre in Imdb database by id"""
    UPDATE_GENRE = """UPDATE genres
                      SET name=%s
                      WHERE id = %s
    """
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_GENRE, (name, id_))
                count = cursor.rowcount
                connection.commit()
        return count
    except Error as err:
        print(err)
        raise


def select_all_genres():
    """Select all genres from Imdb"""
    SELECT_ALL_GENRES = "SELECT * FROM genres"
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ALL_GENRES)
                genres = cursor.fetchall()
        return genres
    except Error as err:
        print(err)
        raise
       


