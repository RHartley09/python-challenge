# Import
import os
import csv
# Read
csvpath = os.path.join("PyPoll", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)