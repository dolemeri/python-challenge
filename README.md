Module 3 Challenge - Python
UofT SCS Data Analytics Bootcamp's - Data Analytics Boot Camp - Assignment 3 (Python)

In this assignment two different projects are given, one of them is a financial report of a company and the other one is the election results. We will try to make a simple and professional report for each project, by using the python script and based on data files have given in a csv file and for each case with a heavy dataset file located in a resource folder. 
PyBank 
In this Challenge, we created a Python script to analyze the financial records of a company. There is a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Our script analyzes the records to calculate each of the following values:
The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period
The results will print into the terminal and also will be sent to a text file for review and reporting.  
In this project, we work with a CSV file (budget_data.csv). First, we specify the correct path to the CSV file and import the necessary modules.
To begin, we define the CSV path and open the file for reading using the with open() statement. This ensures the file is properly opened and later closed after reading its contents. We also define an empty list to store the budget data, then read and convert the data, including the header, into this list.
To calculate the total number of months, I used the len() function to count the entries in the dataset.
For calculating the changes between months, I used a loop to iterate through the list and calculate the month-to-month differences.
To find the average change, I used a for loop to sum the monthly changes and then divided by the number of changes.
To determine the greatest increase and decrease in profits, I used the max() and min() functions along with a lambda function to find the months with the highest and lowest changes.Add the end all results are printed in the terminal and also an output text file.
PyPoll
In this Challenge, the created python script make modernize the vote-counting process of an election.
The script by using a csv file of a given data set of an election called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". We will try to create a Python script that analyzes the votes and calculates each of the following values:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote
The results will print into the terminal and also will be sent to a text file for review and reporting.
In this PyPoll project, similar to our first project, we work with a CSV file (election_data.csv). The correct path to the CSV file needs to be specified, and the required modules must be imported.
First, we define the CSV path and open the file for reading using the with open() statement. This method ensures that the file is properly opened and then closed after reading its contents. The headers are saved after the file is opened.
To create a list of candidates, I extracted their names starting from the third row onward using a for loop. The total number of votes was calculated by iterating through the file and counting the votes for each candidate. This data was stored in a list of candidates which was then sorted.
Using another for loop, I printed the results, including the total number of votes and the average votes per candidate. These results were displayed in the terminal and also saved to an output text file.
