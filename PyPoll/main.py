import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    Voter = []
    Vote =[]

    for row in csvreader:
        Voter.append(row[1])
        Vote.append(row[2])
        
        

        
#Find total months and net total profit/loss
Vote_Total = len(Voter)


print(Vote_Total)