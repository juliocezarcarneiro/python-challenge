# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_input = os.path.join("/", "Users", "Julio", "OneDrive", "Projects", "GitHub_Repositories", "python-challenge", "PyBank", "Resources", "budget_data.csv") # Input file path
file_to_output = os.path.join("/", "Users", "Julio", "OneDrive", "Projects", "GitHub_Repositories", "python-challenge", "PyBank", "analysis", "results.txt") # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
changes = []
previous_profit = None
greatest_increase = ["", 0]
greatest_decrease = ["", 0] 
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_input) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit = int(first_row[1])

    #Process each row of data
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        # Track the total
        total_months +=1
        total_net += profit_loss

        # Track the net change
        change = profit_loss - previous_profit
        changes.append(change)
        previous_profit = profit_loss

    # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase[1]:
            greatest_increase = [date, change]
    
    # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease[1]:
            greatest_decrease = [date, change]

# Calculate the average net change across the months
if len(changes) > 0:
    average_change = sum(changes) / len(changes) # Calculate the average of the changes
else:
    average_change = 0  # Handle the case with no changes

# Generate the output summary
output = (
    f"Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)