import os
import csv
import statistics

total_months = []
total_amount =[]

#Path to collect data
budgetdata_csv = os.path.join('..','Resources','budget_data.csv')

#Read in CSV file 
with open(budgetdata_csv,'r', newline="") as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))

        
#Title
print("Financial Analysis")
print("---------------------")

# The total number of months included in the dataset
#print(len(total_months))
print(f"Total Months: {(len(total_months))}")


# The net total amount of "Profit/Losses" over the entire period
#print(f"Total: $ {(sum(total_amount))}")
print(f"Total: $ {(sum(total_amount))}")

# The average of the changes in "Profit/Losses" over the entire period
#print(statistics.mean(total_amount))
print(f"Average Change: $ {round(statistics.mean(total_amount))}")

# The greatest increase in profits (date and amount) over the entire period
#Only needed for calculation #print(total_amount.index(max(total_amount)))
#print(total_months[25])
#print(max(total_amount))
print(f"Greatest Increase in Profits: {total_months[25], (max(total_amount))}")

# The greatest decrease in losses (date and amount) over the entire period
#print(total_amount.index(min(total_amount)))
#print(total_months[44])
#print(min(total_amount))
print(f"Greatest Decrease in Profits: {total_months[44], (min(total_amount))}")
