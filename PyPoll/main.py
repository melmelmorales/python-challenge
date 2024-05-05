import os
import csv

#This is to output my results to a .txt file
def print_both(file, *args):
    myMessage = ' '.join([str(arg) for arg in args])
    print(myMessage)
    file.write(myMessage + "\n")

# Open and read csv
election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    #Initialize total votes variable and create empty dictionary
    Total_Votes = 0
    Candidates = {}

    # Read through each row of data after the header and find the total number of votes
    for row in csv_reader:
        Total_Votes += 1
        candidate = row[2]
        if candidate in Candidates:
            votes = Candidates[candidate] + 1
            Candidates[candidate] = votes
        else:
            Candidates[candidate] = 1

#This is to output my results to a .txt file

    f = open("output.txt", "w")

    print_both(f, "Election Results")
    print_both(f,'----------------------------')
    print_both(f,"Total Votes: " + str(Total_Votes))
    print_both(f,'----------------------------')


#Finding who the winner is by calcuating total vote counts and percentage for each unique candidate
    max_votes = 0
    winner = ""
    for key in Candidates:
        name = key
        votes = Candidates[key]
        prcnt = votes/Total_Votes*100
        if votes > max_votes:
            max_votes = votes
            winner = name
        print_both(f,name + " {:0.3f}% (".format(prcnt) + str(votes) + ")")
    
    print_both(f,'----------------------------')
    print_both(f,"Winner: " + winner)
    print_both(f,'----------------------------')

    f.close()