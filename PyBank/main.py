import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
 # Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv in default read mode with context manager
with open(csvpath,newline="", encoding="utf-8") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# max and min for montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print the final financial Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = os.path.join("python-challenge", "PyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
#  Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
        

