from mysql.connector import connect, Error
from ..config import connection_detail as cd

# insert_reviewer()'
# It will check:
#               - is reviewer already in database
#               - is movie already in database, if not raise error (can not rate a movie not present in db)
#               - if reviewer already reviewed movie, if true raise error (One rating per reviewer per movie)
#
# If reviewer is not in database add reviewer to reviewer tableadd
# Add rating to rating table


def insert_reviewer(name, email, title, stars):
    "Insert reviewer into IMDB database"
    
    INSERT_REVIEWER = """INSERT INTO reviewers (
                         name, email) 
                         VALUES (%s, %s)"""
    
    INSERT_RATING = """INSERT INTO ratings (
                       movie_id, reviewer_id, stars)
                       VALUES (%s, %s, %s)"""
    
    try:
        reviewer_id = None
        movie_id = None
        row_reviewer = _check_reviewer_by_email(email) 
        row_movie = _check_movie(title)
        if row_reviewer:
           reviewer_id, = row_reviewer  # returning a tuple 

        if row_movie:
            movie_id, = row_movie
        else:
            raise ValueError(f"No Rating: {title} not in database!")

        if reviewer_id and movie_id:
            is_reviewed = _check_reviewer_movie(reviewer_id, movie_id)
            if is_reviewed:
               raise ValueError(f"{name} has already give stars to movie: {title}!")

        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                if not reviewer_id:
                    cursor.execute(INSERT_REVIEWER, (name, email))
                    reviewer_id = cursor.lastrowid  # get id back from inserting reviewer
                    
                cursor.execute(INSERT_RATING, (movie_id, reviewer_id, stars))
                count = cursor.rowcount
                connection.commit()
        return count
    except Error as err:
        print(err)
        raise


def delete_reviewer_by_id(id_):
    """Delete reviewer from Imdb database"""
    DELETE_REVIEWER = """DELETE FROM reviewers
                         WHERE id = %s"""

    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(DELETE_REVIEWER, (id_,))
                count = cursor.rowcount
                cursor.commit()
        return count
    except Error as err:
        print(err)
        raise


def update_reviewer_by_id(id_, name, email):
    """Update reviewer in Imdb database"""
    UPDATE_REVIEWER = """UPDATE reviewers
                         SET name = %s, email = %s 
                         WHERE id = %s"""
    
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_REVIEWER, (name, email, id_))
                count = cursor.rowcount
                cursor.commit()
        return count

    except Error as err:
        print(err)
        raise


def _check_reviewer_by_email(email):
    "Check if reviewer is present in IMDB database"

    SELECT_REVIEWER = """SELECT id FROM reviewers
                         WHERE email = %s"""
    
    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(SELECT_REVIEWER, (email,))
                row = cursor.fetchone()  # If None -> return false
        return row
    except Error as err:
        print(err)
        raise 


def _check_movie(title):
    "Check if movie is present in IMDB database" 
    
    SELECT_MOVIE = """SELECT id FROM movies
                      WHERE title = %s"""

    try:
        with connect(**cd.sql_details) as connection:
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(SELECT_MOVIE, (title, ))
                row = cursor.fetchone()
        return row
    except Error as err:
        print(err)
        raise


def _check_reviewer_movie(reviewer_id, movie_id):
    "Check is reviewer already reviewed movie"
    
    SELECT_REVIEWER_RATING = """SELECT movie_id FROM ratings 
                                WHERE movie_id = %s and reviewer_id = %s"""
    try:  
        with connect(**cd.sql_details) as connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_REVIEWER_RATING, (movie_id, reviewer_id))
                row = cursor.fetchone()
        return row
    except Error as err:
        print(err)
        raise
