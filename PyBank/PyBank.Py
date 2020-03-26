import os
import csv

file = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_profit = 0
monthly_avg_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

prev_pl =0
changes =[]

# Method for Reading the csv into the code 

with open(file) as data:
    csvreader = csv.reader(data, delimiter = ',')
    header=next(csvreader)
    # Defining the location of the important values
    for row in csvreader:
        date = row[0]   
        pl = int(row[1])
        total_profit += pl
        total_months += 1
    #Gettin the change set up where it will not include the first month(January)
        change = pl - prev_pl
        if total_months != 1:
            changes.append(change)
    # Compare the change from the current month to that of the month with the greatest increase
    # variable: if the change is greater than greatest_inc, replace
    # greatest_inc with the new change and update greatest_inc month 
    # with the month from the current row. If tje change is less than greatest_dec,
    # replace greatest_dec with the new change and update greatest_dec month.
    # with month from current row.    
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month =date
        if change <  greatest_dec:
            greatest_dec = change
            greatest_dec_month = date
        # Replace prev_pl with pl for next loop so that the previous year's values carry over
        prev_pl =pl
        first_loop= False
    
    #Calculate the average of the changes over the entire period.
    avg_change = round(sum(changes)/len(changes),2)
    
    # Following line was decprecated due to clarity on instructions.
    # monthly_avg_profit = int(round(total_profit/total_months,0))
    
    #Get the analysis put together
    
    monthly_avg_profit = int(round(total_profit/total_months,0))
    analysis =(
            f"Total Profit: ${total_profit}\n"
            f"Total Months: {total_months}\n"
            f" Average Monthly Profit: ${avg_change}\n"
            f"Greatest Increase: {greatest_inc_month}, ${greatest_inc}\n"
            f"Greatest Decrease: {greatest_dec_month}, ${greatest_dec}\n")
            
            
   
    print(analysis)
    # get the output file set up
    output_file = "output.txt"
    with open(output_file, "w") as doc:
        doc.write(analysis)
