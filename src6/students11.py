
# Writes a CSV file using csv.DictWriter


name = input("What's your name? ")
home = input("Where's your home? ")

import csv

with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
