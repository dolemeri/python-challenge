# This code is a Python script to analyze the financial records of your a company.
# This Python script analyzes the givern records from a CSV file to calculate each of the following values:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#-----------------------------------------------------------------------------------------------------------

#Importing csv  and OS modules

import csv 
import os  


# To read the transfer CSV file, it needs to give the file location path.

cvspath=os.path.join("pyBank","Resources","budget_data.csv")

#creating a list for storing data
budget_data=[]

with open(cvspath) as csvfile:
    reader=csv.DictReader(csvfile)

    # Using loop through data to store in a dictionary that  adds  the definitions into a list (budget_data)
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

#To calculate the total months, we used the len function to count objects in  the data set
total_months=len(budget_data)


#total_months==================================================================================================

# To calculate changes between months we use the loop method through the dictionary
prev_amount=budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"]=budget_data[i]["amount"] - prev_amount
    prev_amount=budget_data[i]["amount"]

#calculate total amount
total_amount=sum(row["amount"] for row in budget_data)


#average change =================================================================================================

#sum over  all of rows of change/total months
total_row_change=sum(row["change"] for row in budget_data)
average=round(total_row_change/(total_months-1),2)

#Calculating Great increase and great decrease ===================================================================

# Here we used lambada function with "change" , max and min to find great increase abd great decrease. 
great_increase=max(budget_data, key=lambda x:x["change"])     #great increase

great_decrease=min(budget_data,key=lambda x:x["change"])      #great decrease


#Print all the info we have gathered
Final_Report=[("Financial Analysis "),
(f'Total Months: {total_months}'),
(f'Total: {total_amount}'),
(f'Average Change: {average}'),
(f'Greatest Increase in Profits: {great_increase["month"]} ${great_increase["change"]}'),
(f'Greatest Decrease in Profits: {great_decrease["month"]} ${great_decrease["change"]}')]
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
print(Final_Report,'\n')
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#======================================================================================================
# Transfer the data and results to a text file in the name of pybank_analysis.txt

file_output=os.path.join("pyBank","Resources","pyBank_analysis.txt")

with open(file_output,"w") as textfile:
    print("Financial Analysis",file=textfile)
    print("----------------------", file=textfile)
    print(f'Total Months: {total_months}',file=textfile)
    print(f'Total: $ {total_amount}',file=textfile)
    print(f'Average Change: $ {average}',file=textfile)
    print(f'Greatest Increase in Profits: {great_increase["month"]} (${great_increase["change"]})', file=textfile)
    print(f'Greatest Decrease in Profits: {great_decrease["month"]} (${great_decrease["change"]})', file=textfile)
