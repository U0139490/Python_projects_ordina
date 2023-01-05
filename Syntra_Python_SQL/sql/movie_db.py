from mysql.connector import connect, Error
from ..config import connection_detail as cd
from pathlib import Path
import json


def insert_movie(title, language, duration, release_year, summary):
    """Insert movie in IMDB database"""

    SQL_INSERT = """INSERT INTO movies (
                    title, language, duration, release_year, summary)
                    VALUES (%s, %s, %s, %s, %s)"""
    
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                        SQL_INSERT,(title, language, duration, release_year, summary)
                )
                count = cursor.rowcount
                connection.commit()
        return count 
    except Error as err:
        print(err)
        raise
 

def insert_movies_from_json(filename):
    """Insert movies from json file"""

    SQL_INSERT = """INSERT INTO movies (
                    title, language, duration, release_year, summary)
                    VALUES (%s, %s, %s, %s, %s)"""

    if not Path(filename).exists():
        raise ValueError(f"Filename {filename} doesn't exists")
    
    try:
        with open(filename, 'r') as file:
            movies = json.load(file)
            data = [ 
                    (movie['title'], movie['language'], movie['duration'], movie['release_year'], movie['summary'])
                    for movie in movies
            ]

        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(SQL_INSERT, data)
                count = cursor.rowcount
                connection.commit()
        return count
    except (IOError, Error) as err:
        print(err)
        raise


# This will collect all movies (id, title, release_year) from movies table and calculate average stars from ratings table
def select_all_movies():
    """Select id, title, release_year, average stars for all movies"""

    SELECT_MOVIES = """SELECT id, title, release_year, stars
                       FROM movies LEFT JOIN (SELECT movie_id, AVG(stars) as 'stars'
                                              FROM ratings
                                              GROUP BY movie_id) as sub
                       ON movies.id = sub.movie_id 
                       ORDER BY stars DESC"""
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_MOVIES)
                return cursor.fetchall()
    except Error as err:
        print(err)
        raise err


# When you click on a movie from 'select_all_movies', this will 
# retrieve all info for one movie
def select_one_movie(id_):
    "Retrieve all info for one movie"
    
    SELECT_MOVIE = """SELECT title, language, duration, release_year, summary, director_id
                      FROM movies 
                      WHERE id = %s"""

    SELECT_DIRECTOR = """SELECT name , birth_year, gender
                         FROM persons
                         WHERE id = %s"""
    
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_MOVIE, (id_, ))
                row_movie = cursor.fetchone()
                
                if row_movie:
                    title, language, duration, release_year, summary, director_id = row_movie
                    cursor.execute(SELECT_DIRECTOR, (director_id, ))
                    row_director = cursor.fetchone()

                    name, birth_year, gender = None, None, None

                    if row_director:
                        name, birth_year, gender = row_director
                    return (
                            title, language, duration, release_year,
                            summary, name, birth_year, gender
                            )
                else:
                    raise ValueError(f"movie with id: {id_} not present in imdb database")
    except Error as err:
        print(err)
        raise


def delete_movie_by_id(id_):
    """Delete a movie from Imdb database by id"""
    DELETE_MOVIE = "DELETE FROM movies WHERE id = %s"
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(DELETE_MOVIE, (id_,))
                count = cursor.rowcount
                connection.commit()
        return count
    except Error as err:
        print(err)
        raise



def update_movie_by_id(id_, title,language,duration,release_year,summary):
    """Update a movie in Imdb database by id"""
    UPDATE_MOVIE = """UPDATE movies
                      SET title=%s, language=%s, duration=%s, release_year=%s, summary=%s
                      WHERE id = %s
    """
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_MOVIE, (title,language,duration, release_year, summary, id_))
                count = cursor.rowcount
                connection.commit()
        return count
    except Error as err:
        print(err)
        raise
