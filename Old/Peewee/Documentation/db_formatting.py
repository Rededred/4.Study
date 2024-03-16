from peewee import *

from datetime import date

db = SqliteDatabase('people.db')

db.connect()


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


db.create_tables([Person, Pet])

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save()  # bob is now stored in the database

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

grandma.name = 'Grandma L.'
grandma.save()  # Update grandma's name in the database

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_rj = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

herb_mittens.delete_instance()  # he had a great life

herb_fido.owner = uncle_bob
herb_fido.save()

grandma = Person.select().where(Person.name == 'Grandma L.').get()
grandma = Person.get(Person.name == 'Grandma L.')  # retrieve Grandma’s record from the database


for person in Person.select():
    print(person.name)

query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)
'''
for pet in Pet.select().where(Pet.owner == uncle_bob):
    print(pet.name)
'''
