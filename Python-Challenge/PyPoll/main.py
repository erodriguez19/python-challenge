# import os
# import csv

# #Script for CSV path
# csvpath = os.path.join("Resources","election_data.csv")
# file_to_output = os.path.join("Analysis", "election_analysis.txt")

# candidate_option = []
# candidate_votes = {}
# total_votes = 0
# winner = ""
# winner_votes = 0

# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)

#     for row in csvreader:
#           candidate = row[2]
#           if candidate not in candidate_option:
#                candidate_option.append(candidate)
#                candidate_votes[candidate] = 0
#           candidate_votes[candidate] += 1
#           total_votes += 1



# with open(file_to_output, 'w') as txtfile:

#     output = (
#         f'Election Results\n'
#         f'-------------------------\n'
#         f'Total Votes: {total_votes}\n'
#         f'-------------------------\n'
#             )
#     txtfile.write(output)
#     print(output)


#     for name in candidate_option:
#         percentage= (round(candidate_votes[name] / total_votes * 100, 3))
#         output = f"{name}: {percentage}% ({candidate_votes[name]})\n"
#         txtfile.write(output)
#         print(output)
        
#         #If statement to determine winner [Whatever name has the most rows print that name as the winner]
#         if candidate_votes[name] > winner_votes: #If charles has the biggest number print charles as the winner
#             winner_votes = candidate_votes[name]
#             winner = name

#     #Print output for winner
#         output = (
#         f'-------------------------\n'
#         f'Winner: {winner}\n'
#         f'-------------------------\n'
#             )
#     txtfile.write(output)
#     print(output)
