# CSV file
import csv

with open('data.csv') as csvfile:
    reader = csv.read(csvfile)
    for row in reader:
        print(row)