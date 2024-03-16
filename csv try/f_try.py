import csv
with open('weather.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
