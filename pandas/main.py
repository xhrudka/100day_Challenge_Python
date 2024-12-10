import pandas
import csv
file_path = r"C:\Users\marti\OneDrive\Documents\GitHub\100day_Challenge_Python\pandas\weather_data.csv"

with open (file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        print(row)
#  data = pandas.read_csv("weather_data.csv")
#print(data)