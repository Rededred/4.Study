from peewee import *

db = SqliteDatabase('db/database.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class Expense(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'expense'

class Payment(BaseModel):
    amount = FloatField()
    payment_date = DateField()
    expense_id = ForeignKeyField(Expense)

    class Meta:
        db_table = 'payments'