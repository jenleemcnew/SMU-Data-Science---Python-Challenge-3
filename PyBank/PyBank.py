import os
import csv

#Constants
INPUT_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "budget_results.txt")

# #Varibles
total_months = 0
total_net_profits = 0
prior_profit_loss = None
profit_change = 0
greatest_increase = ["", -9999999999]
greatest_decrease = ["", +9999999999]
change_list = []


# Change Directory to script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(INPUT_PATH) as data:
    reader = csv.reader(data)
    header = next(reader)
    first_row = next(reader)

    # # For Loop - Calculate Total Months/Profit/Loss
    for row in reader:
        current_month = row[0]
        current_profit_loss = int(row[1])
        total_months += 1
        total_net_profits += current_profit_loss
  
        #change in profit
        if prior_profit_loss is not None:
            profit_change = current_profit_loss - prior_profit_loss
            change_list.append(profit_change)

            #If - check for greatest increase, greastest decrease
            if profit_change > greatest_increase[1]:
                greatest_increase[0] = current_month
                greatest_increase[1] = profit_change
                
            if profit_change < greatest_decrease[1]:
                greatest_decrease[0] = current_month
                greatest_decrease[1] = profit_change
              
            prior_profit_loss = current_profit_loss
        
# Calculate Average Change
if change_list:
    average_change = sum(change_list) / len(change_list)
else:
    average_change = 0 
                
   # Write the financial analysis results to the file
with open(OUTPUT_PATH, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_net_profits}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net_profits}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

