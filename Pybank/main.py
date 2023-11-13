import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    Month = []
    Profit_Loss=[]
    Profit_change = []

    for row in csvreader:
        Month.append(row[0])
        Profit_Loss.append(int(row[1]))
        
#Find total months and net total profit/loss
Month_Total = len(Month)
Net_Profit= sum(Profit_Loss)

#Find Average Change
for i in range (1, Month_Total):
     change= Profit_Loss[i] - Profit_Loss[i-1]
     Profit_change.append(change)

Average_Change = sum(Profit_change)/len(Profit_change)

#Greatest Increase
Greatest_Increase= max(Profit_change)

#Greastest Decrease
Greatest_Decrease= min(Profit_change)

#Profit_Loss_Average = (sum(Profit_Loss)/len(Profit_Loss))
#Greatest_Increase= max(Profit_Loss)
#Greatest_Decrease= min(Profit_Loss)

print(Month_Total)
print(Net_Profit)
print(Average_Change)
print(Greatest_Increase)
print(Greatest_Decrease)
    
#print(row(Greatest_Increase))
#print(row(Greatest_Decrease))
    
