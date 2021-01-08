# Add our dependencies
import os
import csv

# Assign a variable to load the file to a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

# To Do: read and analyze the data here
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)
#    # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)

# Close the file
# election_data.close()


# Using the open() function with the w mode we will write data to the file
# open(file_to_save, "w")

# Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

# # Write some data to the file
#     txt_file.write("Counties in the Election"
#     "\n----------------------\n" "Arapahoe\nDenver\nJefferson")
