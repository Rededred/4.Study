import datetime
from models import *

# Core Functionality
with db:
    kommunalka = Expense(name = 'Коммуналка').save()
    benzin = Expense.create(name = 'Бензин').save()
    inet = Expense.insert(name = 'Интернет').execute()

print('DONE')