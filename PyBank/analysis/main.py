#Import os
import os
#Import csv 
import csv

# Lists to store data
total_months = 0
total_profit_loss = 0
monthly_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]
dates = []
profits = []

# Set path for file
csvpath = os.path.join("PyBank","Resources","budgetdata.csv")

#Read csv 
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
   
   # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

#Loop through
    for row in csvreader:
    # Append date and profit/loss to their respective lists
        dates.append(row[0])
        profit_loss = int(row[1])
        profits.append(profit_loss)

        # Update total profit/loss
        total_profit_loss += profit_loss

    # Calculate monthly changes and update total months
    total_months = len(dates)
    for i in range(1, total_months):
        monthly_change = profits[i] - profits[i - 1]
        monthly_change_list.append(monthly_change)

        # Check for greatest increase and decrease
        if monthly_change > greatest_increase[1]:
            greatest_increase = [dates[i], monthly_change]
        if monthly_change < greatest_decrease[1]:
            greatest_decrease = [dates[i], monthly_change]

# Calculate average change
average_change = sum(monthly_change_list) / (total_months - 1) if total_months > 1 else 0

# Prepare output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print output
print(output)

