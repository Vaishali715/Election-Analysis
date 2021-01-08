# Add our dependencies
import os
import csv

# Assign a variable to load the file to a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

# To Do: read and analyze the data here
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
# Print each row in the CSV file
    for row in file_reader:
    # Add to the total vote count
        total_votes += 1
    # Print the candidate name from each row
        candidate_name = row[2]

    # If the candidate name does not match any existing..
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts
        # 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    # 2. Retrieve vote count for a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: Print out each candidate's name, vote count and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the vote count is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"Winning percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    
