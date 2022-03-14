import mysql.connector
from mysql.connector import Error
import pandas as pd

pw = "jeSt3B3f"
db = "preschool"

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("localhost","root",pw)



create_server_connection("localhost","root",pw)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE preschool"
create_database(connection, create_database_query)

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


create_child_table = """
CREATE TABLE child (
  child_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  age INT,
  hours INT,
  grant_hours INT
  );
 """

create_parent_table = """
CREATE TABLE parent (
    parent_id INT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL
    
    );
   """

create_customer_table = """
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    telephone INT NOT NULL,
    address VARCHAR(40) NOT NULL,
    email VARCHAR(40)

    );
   """


connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
execute_query(connection, create_child_table) # Execute our defined query
execute_query(connection, create_parent_table)
execute_query(connection, create_customer_table)

pop_parent = """
INSERT INTO teacher VALUES
(1,  'James', 'Smith'),
(2, 'Stefanie',  'Martin' ), 
(3, 'Steve', 'Wang'),
(4, 'Friederike',  'Müller-Rossi'),
(5, 'Isobel', 'Ivanova'),
(6, 'Niamh', 'Murphy');
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, pop_parent)