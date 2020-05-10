# Import
import os
import csv
# Read
csvpath = os.path.join("PyBank", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

# Total Months
getMonths = []

totalMonths = (row[0]).split(" ")
length.append(float(totalMonths[0]))
print(totalMonths) 
