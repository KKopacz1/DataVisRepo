import os
import csv

#Grab Election Data 1
election_data_1 = os.path.join('election_data_1.csv')

#Grab Election Data 2
election_data_2 = os.path.join('election_data_2.csv')

#Set Variables for Candidates
Vestal_Count = 0
Torres_Count = 0
Seth_Count = 0
Cordin_Count = 0

with open(election_data_1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through counting votes
    for row in csvreader:
        if row[2] == "Vestal":
            Vestal_Count = Vestal_Count + 1
        elif row[2] == "Torres":
        	Torres_Count = Torres_Count + 1
        elif row[2] == "Seth":
        	Seth_Count = Seth_Count + 1
        else:
        	Cordin_Count = Cordin_Count + 1

    Total_Votes = Vestal_Count + Torres_Count + Seth_Count + Cordin_Count
    Vestal_Percent = (Vestal_Count/Total_Votes)*100
    Torres_Percent = (Torres_Count/Total_Votes)*100
    Seth_Percent = (Seth_Count/Total_Votes)*100
    Cordin_Percent = (Cordin_Count/Total_Votes)*100

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(Total_Votes))
    print("-------------------------")
    print("Vestal: " + str(Vestal_Percent) + "% (" + str(Vestal_Count) + ")")
    print("Torres: " + str(Torres_Percent) + "% (" + str(Torres_Count) + ")")
    print("Seth: " + str(Seth_Percent) + "% (" + str(Seth_Count) + ")")
    print("Cordin: " + str(Cordin_Percent) + "% (" + str(Cordin_Count) + ")")
    print("-------------------------")
    print("Vestal Wins!")


