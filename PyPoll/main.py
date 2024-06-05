import os

import csv

#csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
csvpath = os.path.abspath("C:/Users/kgonz/OneDrive/Desktop/UNC_DA_Bootcamp/github repositories/Module 3_python-challenge/PyPoll/Resources/election_data.csv")
print(csvpath)

total_votes = []
stockham_votes = 0
degette_votes = 0
doane_votes = 0

with open(csvpath, encoding="UTF-8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csv_header =next(csvreader)
    for row in csvreader: 
        total_votes.append(row[0])

        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes +=1

candidates = ["Charles Casper Stockham", "Diane DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham_votes, degette_votes, doane_votes]
votes_dict = dict(zip(candidates, candidate_votes))
winner = max(votes_dict, key=votes_dict.get)

total_vote_count =len(total_votes)

stockham_percent =(stockham_votes/total_vote_count) * 100
degette_percent = (degette_votes/total_vote_count) * 100
doane_percent = (doane_votes/total_vote_count) * 100

print("Election Results")
print("------------------------")
print(f"Total Votes: {len(total_votes)}")
print("------------------------")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

#analysis = os.path.join("PyPoll", "Analysis", "Election_Analysis.txt")
analysis = os.path.abspath("C:/Users/kgonz/OneDrive/Desktop/UNC_DA_Bootcamp/github repositories/Module 3_python-challenge/PyPoll/Resources/Election_Analysis.txt")

with open(analysis, "w") as file:

    file.write("Election Result")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes : {len(total_votes)}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")

 