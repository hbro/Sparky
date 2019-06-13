from peewee import *
import logging
import datetime

db = SqliteDatabase("Sparky.db")
logger = logging.getLogger(__name__)

class Memory(Model):
    id = PrimaryKeyField()
    type = CharField()
    key = CharField()
    value = TextField()

    class Meta:
        database = db

class MemoryTransaction(Model):
    id = PrimaryKeyField()
    type = CharField()
    memory_id = ForeignKeyField(Memory, backref="memory_transactions")
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    logger.debug("This is a test")
    db.connect()
    db.create_tables([Memory,MemoryTransaction], safe=True)