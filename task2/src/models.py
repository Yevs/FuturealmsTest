from datetime import datetime

from peewee import *

db = SqliteDatabase('messages.db')

class Message(Model):
    message = CharField(null=False)
    response = CharField(null=False)
    created = DateTimeField(default=datetime.now)

    class Meta:
        database = db