#This Python script analyzes the votes and calculates each of  a vote-counting process that will give out the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote
#-------------------------------------------------------------------------------------------------------------------------------

# Importing CSV and os Modules
import csv 
import os 

# To read the transfer CSV file, it needs to give the file location path.

pathfile=os.path.join("pyPoll","Resources","election_data.csv")

#Opening the CSV file, making it readable, and extracting the header row.
#  
with open(pathfile, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)

#==============================================================================================================

#Creating a list of candidates by extracting their names from the second row onwards in the file    
    candidate_roster=[candidate[2] for candidate in csvreader]

#Calculating the total numbers of votes 
vote_total=len(candidate_roster)


# Determining the totla votes of each candidate by yousing the List of candidate roster file. 

candidate_votes=[[candidate,candidate_roster.count(candidate)] for candidate in set(candidate_roster)]

# Sorting the candidate as their numbers of votes by using the lambada function 

candidates_sorted=sorted(candidate_votes, key=lambda x:x[1], reverse=True)


#================================================================================================================

# Using the sorted list, announce the winner and other top candidates in order, along with their respective percentages.

print("--------------------------------------------\n")
print("Total Votes :  " + str(vote_total) + '\n')
print("--------------------------------------------\n")
print("The candidates who recieved The votes: \n")
for candidate in candidates_sorted:
    percentage=(candidate[1]/vote_total)*100
    print(f'{candidate[0]}       {percentage:6.3f}%   ({candidate[1]}) \n')
print(f'Winner :  {candidates_sorted[0][0]} ')
print("--------------------------------------------")
# Make an analys ouput file and write the results ito it.
analysis_file=os.path.join("pyPoll","Resources","pyPoll_analysis.txt")

with open(analysis_file, "w") as txtfile:
     print("Election results", file=txtfile)

     print("--------------------------------------------\n", file=txtfile)
     print("Total votes  "+ str(vote_total), file=txtfile)
     print("\n", file=txtfile)
     
     print("--------------------------------------------\n", file=txtfile)
    
     for candidate in candidates_sorted:
        percentage=(candidate[1]/vote_total)*100
        print(f'{candidate[0]}: {percentage:6.3f}% ({candidate[1]}) ', file=txtfile)
     print("", file=txtfile)
     print("--------------------------------------------\n", file=txtfile)   
     print(" Winner  :  " + candidates_sorted[0][0] , file=txtfile)