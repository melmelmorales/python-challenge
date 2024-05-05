import os
import csv

#This is to output my results to a .txt file
def print_both(file, *args):
    myMessage = ' '.join([str(arg) for arg in args])
    print(myMessage)
    file.write(myMessage + "\n")

# Open and read csv
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)

    #Initializing all of my variables
    Months = 0
    Total = 0
    Average_Change= 0
    Greatest_Profit_Increase = 0
    Greatest_Profit_Increase_Day = ""
    Greatest_Profit_Decrease = 0
    Greatest_Profit_Decrease_Day = ""
    prev = 0
    Change_Total = 0

    # Count the months and calculate the sum of total profits, and then calculate average change
    for row in csv_reader:
        Months += 1
        profit = int(row[1])
        Total += profit
        Average_Change = Total/Months
        
        #Skip the first entry and then calculate the change: "final - initial" or profit - prev. Sum all of the changes and then find the Max and Min Profit change 
        if(Months != 1):
            change = profit - prev
            Change_Total += change
            if (change >= Greatest_Profit_Increase):
                Greatest_Profit_Increase = change
                Greatest_Profit_Increase_Day = row[0]

            if (change <= Greatest_Profit_Decrease):
                Greatest_Profit_Decrease = change
                Greatest_Profit_Decrease_Day = row[0]

        prev = profit    

    #Calculate the average change
    Average_Change = Change_Total/(Months-1)

    #Export to terminal and .txt
    f = open("output.txt", "w")

    print_both(f, "Financial Analysis")
    print_both(f, '----------------------------')
    print_both(f, "Total Months: " + str(Months))
    print_both(f, "Total: $" + str(Total))
    print_both(f, "Average Change: ${:0.2f}".format(Average_Change))
    print_both(f, "Greatest Increase In Profits: " + Greatest_Profit_Increase_Day + "($ " + str(Greatest_Profit_Increase) + ")")
    print_both(f, "Greatest Decrease In Profits: " + Greatest_Profit_Decrease_Day + "($ " + str(Greatest_Profit_Decrease) + ")")    

    f.close()