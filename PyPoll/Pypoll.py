import os
import csv
import math
file = os.path.join("Resources", "election_data.csv")
print("Election Results")
print("__________________")
votes = []
candidates = []




# Method for Reading using CSV module

with open(file) as data:
    # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(data, delimiter = ',')
    # Read the header row first (skip this step if there is no header)
   
   csv_header = next(csvreader)
   
    # Read the header row first (skip this step if there is no header)

   for column in csvreader:
       votes.append(column[0])
       candidates.append(column[2])
   
   # Set up a dictionary to keep up with the candidates.
   Dict = {"1":"Khan", "2":"Correy", "3":"Li", "4":"O'Tooley" }
   
   # Count the number of votes then then get them on the terminal
   Total_Votes = (len(votes))
   print(f"Total Votes: {Total_Votes}")
   print("__________________")
   
   #Count the number of times each candidate appears in the list
   Khan = int(candidates.count(Dict["1"]))
   Correy = int(candidates.count(Dict["2"]))
   Li = int(candidates.count(Dict["3"]))
   O_Tooley = int(candidates.count(Dict["4"]))
   
   #Find the percentage of the vote that each candidate got 
   Khan_percentage = round((Khan/Total_Votes) * 100, 1)
   Correy_percentage = round((Correy/Total_Votes) * 100,1) 
   Li_percentage = round((Li/Total_Votes) * 100, 5)
   O_Tooley_percentage = round((O_Tooley/Total_Votes) * 100, 5)
   
   #Print each candidate's name, vote percentage, and the number of votes they won
   print(f"Khan: {Khan_percentage}% ({Khan})")
   print(f"Correy: {Correy_percentage}% ({Correy})")
   print(f"Li: {Li_percentage}% ({Li})")
   print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")
    #Compare the vote total for each candidate and then pick a winner! 
   if Khan > Correy > Li > O_Tooley:
       Winner = "Khan"
   elif Correy > Khan > Li > O_Tooley:
       Winner = "Correy"
   elif Li > Khan > Correy > O_Tooley:
       Winner = "Li"
   elif O_Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"
   print(f"Winner: {Winner}")

#Get the analysis printed into a text file
   output_path = os.path.join("analysis.txt")
with open(output_path, 'w', newline='') as txtfile:
   txtfile.write(f"Total Votes: {Total_Votes}")
   txtfile.write(f"Khan: {Khan_percentage}% ({Khan})")
   txtfile.write(f"Correy: {Correy_percentage}% ({Correy})")
   txtfile.write(f"Li: {Li_percentage}% ({Li})")
   txtfile.write(f"O'Tooley: {O_Tooley_percentage}% ({Correy})")
   txtfile.write(f"Winner: {Winner}")
   txtfile.close()