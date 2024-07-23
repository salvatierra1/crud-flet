from peewee import Model, CharField, IntegerField, AutoField
from database.db import db

class Student(Model):
    id = AutoField()
    name = CharField()
    last_name = CharField()
    age = IntegerField()
    
    class Meta:
            database = db
    
db.connect()
db.create_tables([Student])
