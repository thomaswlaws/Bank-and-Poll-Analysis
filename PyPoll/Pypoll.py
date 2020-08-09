# Imports
import os
import csv
import math
file = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis","election_analysis.txt")
print("Election Results")
print("__________________")

candidate_votes = {}
votes = 0    


# Method for Reading using CSV module

with open(file) as data:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(data, delimiter = ',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   
    # Read the header row first (skip this step if there is no header)

    for column in csvreader: 
        votes += 1
        candidates = column[2]
        if candidates in candidate_votes.keys():
            candidate_votes[candidates]+=1
        else:
            candidate_votes[candidates]=1
   
   # Count the number of votes then then get them on the terminal
with open(file_to_output, "w") as text_file:
    Total_Votes = votes 
    print(f"Total Votes: {Total_Votes}")
    print("__________________")
    # Count the number of votes for each candidate and calculate the percentage each candidate got
    total=(f"Total Votes: {Total_Votes}\n"
           "__________________\n")
    text_file.write(total)       
    for candidate, votes in candidate_votes.items():
        percent = round((float(votes)/Total_Votes) * 100 , 2)
        print(f" {candidate} : {percent}% ({votes})")
        output=(f" {candidate} : {percent}% ({votes})\n")
        text_file.write(output)    
    #  Find the candidate with the most votes
    for key in candidate_votes.keys():
        if candidate_votes[key] == max(candidate_votes.values()):
            winner = key
    print (f"Winner: {winner}")
    winner_output = (f"Winner: {winner}")
    text_file.write(winner_output)
   
   
   
 


   

  
