#Import os
import os
#Import csv 
import csv

# Lists to store data
total_months = []
total_amount = []
average_change = []


#csvpath = os.path.join("PyBank","Resources","budgetdata.csv")
csvpath = os.path.abspath("C:/Users/kgonz/OneDrive/Desktop/UNC_DA_Bootcamp/github repositories/Module 3_python-challenge/PyBank/Resources/budgetdata.csv")
print(csvpath)

with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))
        #loop through each profit change to calculate average change 
    for i in range(len(total_amount)-1):
       average_change.append(total_amount[i+1]-total_amount[i]) 

greatest_increase = max(average_change)
greatest_decrease = min(average_change)

greatest_increase_month = average_change.index(max(average_change)) + 1
greatest_decrease_month = average_change.index(min(average_change)) + 1

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months : {len(total_months)}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
print(f'Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))}')
print(f'Greatest decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))}')

#analysis = os.path.join("PyBank","Analysis", "Financial_Analysis.txt")
analysis = os.path.abspath("C:/Users/kgonz/OneDrive/Desktop/UNC_DA_Bootcamp/github repositories/Module 3_python-challenge/PyBank/Resources/Financial_Analysis.txt")
with open(analysis, "w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------------------")
    file.write("\n")
    file.write(f"Total Months : {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))}")
    file.write(f"Greatest decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))}")




