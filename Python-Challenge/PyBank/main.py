import os
import csv

#Script for CSV path
csv_path = os.path.join("Resources","budget_data.csv")


with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
            print(row)

#Total months
with open(csv_path, 'r') as fp:
     lines = sum(1 for line in fp) - 1

#Total Profit/Losses

greatest_increase = ["",0]
greatest_decrease = ["", 9999999999999999999]

netchange_list = []
with open(csv_path, 'r') as fp:
     csvfile = csv.reader(fp)
     header_row = next(csvfile)
     first_row = next(csvfile)
     first_r = int(first_row[1])
     aveChange = int(first_row[1])
     for row in csvfile:
        first_r += int(row[1])
        netchange = (int(row[1]) - aveChange) #total math
        aveChange = int(row[1])
        netchange_list += [netchange]
        sum(netchange_list)
        Sum_List = sum(netchange_list) / (len(netchange_list)) #Average change math
# Greatest increase and decrease


        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange
        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange


print("Total: $"+str(first_r)) #total
print("Average Change: $"+ str(round(Sum_List, 2))) #Average Change
print(greatest_increase) #Greatest Increase
print(greatest_decrease) #Greatest Decrease

#Output for text file
TextF_path = os.path.join("Analysis", "Text_file.txt")

with open(TextF_path,"w") as txt_file:
    TXTwriter = csv.writer(txt_file, delimiter=',')
    Output = (f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {lines}\n"
    f"Total: ${first_r}\n"
    f"Average Change: ${Sum_List:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

    print(Output)
    txt_file.write(Output)
 
