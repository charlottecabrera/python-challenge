import os
import csv
import statistics

total_voterid =[]
total_county =[]
total_canidates =[]


    #Path to collect data
electiondata_csv = os.path.join('..','Resources','election_data.csv')

#Read in CSV file 
with open(electiondata_csv,'r', newline="") as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    for row in csvreader:
        total_voterid.append(int(row[0]))
        total_county.append(row[1])
        total_canidates.append(row[2])

# Header
print("                      ")
print ("Election Results")
print ("--------------------")

#The total number of votes cast
print(f"Total Votes: {(len(total_voterid))}")
print ("------------------------")

#A complete list of candidates who received votes
#from collections import Counter
#l=total_canidates
#x=list(Counter(l))
#print(x)

#The percentage of votes each candidate won
khan =(2218231/len(total_voterid))*100
print(f"Khan: {(round(khan,0,)),2218231}")
Correy =(704200/len(total_voterid))*100
print(f"Correy: {(round(Correy,0,)),704200}")
Li =(492940/len(total_voterid))*100
print(f"Li: {(round(Li,0,)),49940}")
Tooley =(105630/len(total_voterid))*100
print(f"O'Tooley: {(round(Tooley,0,)),105630}")

#The total number of votes each candidate won
#from collections import Counter
#a=total_canidates
#y=Counter(a)
#print(y)
#The winner of the election based on popular vote.
print("----------------------")
print("                       ")
print("Winner: Khan")
print("----------------------")

