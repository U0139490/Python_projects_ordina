import hashlib
#PBKDF2 is a modern hashing algorithm that is being used nowadays since it has a considerable computational cost which reduces the vulnerabilities of brute force attacks.
from hashlib import pbkdf2_hmac as pbkdf2
from key import password_sql 
import mysql.connector as msql
from mysql.connector import Error
import os
"""
https://www.youtube.com/watch?v=--tnZMuoK3E&ab_channel=Seytonic
"""

"""
With regular cryptographic hash functions (e.g. MD5, SHA256), 
an attacker can guess billions of passwords per second. 
With PBKDF2, bcrypt, or scrypt, the attacker can only make a 
few thousand guesses per second (or less, depending on 
the configuration).
"""
def create_hash(password, salt):
    #https://levelup.gitconnected.com/python-salting-your-password-hashes-3eb8ccb707f9
    #Python String encode() converts a string value into a collection of bytes, using an encoding scheme specified by the user.
    plaintext = password.encode()
    digest = pbkdf2('sha256', plaintext, salt, 100000)
    hex_hash = digest.hex()
    return hex_hash


def create_connection():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': password_sql,
        'database': 'social_media'
        }
    conn = msql.connect(**config)
    return conn

def store_user(username, password):
    salt=os.urandom(32)
    hashed_password = create_hash(password,salt)
   
    conn = create_connection()
    if conn.is_connected():
        cursor = conn.cursor()       
        query = f'''call insert_user( %s, %s, %s);'''
        val = (username, hashed_password, salt.decode('latin1'))
        cursor.execute(query,val)
        conn.commit()
        conn.close()

def check_password(userid, userPassword):
    conn = create_connection()
    sql = f'''call get_user({userid})'''
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    hash_password_InDB = result[2]

    salt = result[3].encode('latin1')
    hex_hash = create_hash(userPassword,salt)
    return hex_hash == hash_password_InDB

print(check_password(8, "test123"))



# """
# PBKDF2 applies a pseudorandom function, 
# such as hash-based message authentication code (HMAC), 
# to the input password or passphrase along with a salt 
# value and repeats the process many times to produce a 
# derived key, which can then be used as a cryptographic 
# key in subsequent operations.

# """

# """
# Alle gewone ASCII-codes maken deel uit van de UTF-8 character set. 
# UTF-8 is uitgegroeid tot het standaard coderingssysteem voor het 
# uitwisselen van digitale tekst, zoals e-mails, webpagina's of 
# databasegegevens


# UTF-8 encodes a character into a binary string of one, two, three, or four bytes. 
# UTF-16 encodes a Unicode character into a string of either two or four bytes. 
# This distinction is evident from their names. 
# In UTF-8, the smallest binary representation of a character 
# is one byte, or eight bits.

# """