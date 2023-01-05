from mysql.connector import connect, Error


# SQL Statements
CREATE_DATABASE = "CREATE DATABASE IF NOT EXISTS imdb"

USE_DATABASE = "USE imdb"

CREATE_TABLE_PERSON = """CREATE TABLE IF NOT EXISTS persons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    birth_year YEAR(4) NOT NULL,
    gender VARCHAR(1)
)"""

CREATE_TABLE_MOVIES = """CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    language VARCHAR(50),
    duration FLOAT,
    release_year YEAR(4),
    summary VARCHAR(500),
    director_id INT,
    FOREIGN KEY(director_id) REFERENCES persons(id) ON DELETE SET NULL
)"""

CREATE_TABLE_REVIEWERS = """CREATE TABLE IF NOT EXISTS reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    name VARCHAR(25) NOT NULL,
    UNIQUE(email)
)"""

# These will go back later in CREATE_TABLE_REVIEWERS (temporaly used to test for login with salt and hash)  
# password VARCHAR(100) NOT NULL,
# salt VARCHAR(100) NOT NULL

CREATE_TABLE_RATINGS = """CREATE TABLE IF NOT EXISTS ratings (
    movie_id INT,
    reviewer_id INT,
    stars INT NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id),
    CHECK (stars >= 0 and stars <=10)
)"""

CREATE_TABLE_GENRES = """CREATE TABLE IF NOT EXISTS genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25) NOT NULL
)"""

CREATE_TABLE_MOVIE_GENRE = """CREATE TABLE IF NOT EXISTS movie_genre (
    movie_id INT,
    genre_id INT,
    FOREIGN KEY(movie_id) REFERENCES movies(id) ON DELETE CASCADE,
    FOREIGN KEY(genre_id) REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY(movie_id, genre_id)
)"""

CREATE_TABLE_ACTORS = """CREATE TABLE IF NOT EXISTS actors (
    movie_id INT,
    person_id INT,
    role_name VARCHAR(50) NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES movies(id) ON DELETE CASCADE,
    FOREIGN KEY(person_id) REFERENCES persons(id) ON DELETE CASCADE,
    PRIMARY KEY(movie_id, person_id)
)"""


def create_tables_imdb(connection_details):
    """Create Database & Tables for imdb"""
    try:
        with connect(**connection_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_DATABASE)
                cursor.execute(USE_DATABASE)
                cursor.execute(CREATE_TABLE_PERSON)
                cursor.execute(CREATE_TABLE_MOVIES)
                cursor.execute(CREATE_TABLE_REVIEWERS)
                cursor.execute(CREATE_TABLE_RATINGS)
                cursor.execute(CREATE_TABLE_GENRES)
                cursor.execute(CREATE_TABLE_MOVIE_GENRE)
                cursor.execute(CREATE_TABLE_ACTORS)
                connection.commit()
    except Error as e:
        print(e)
        raise





