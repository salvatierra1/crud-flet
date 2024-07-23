from peewee import MySQLDatabase

#Local
db = MySQLDatabase(
    'db-flet',  
    user='root',  
    password='',   
    host='localhost', 
    port=3306  
)
