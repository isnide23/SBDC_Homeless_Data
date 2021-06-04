import csv
import pandas as pd

# Open the file and start the CSV reader
file = open("data.csv", "r")
reader = csv.reader(file)

responses = []  # This is a list of a responses (responses are dictionaries, see below)
headers = next(reader)  # This is a list that has all of the first row headers

count = 0  # Count keeps track of which row we are on
for row in reader:  # Iterate through each row after the headers
    count += 1
    if count % 2 != 0:  # Skip every other row because it's blank
        continue
    response = {}  # Response is a dictionary where the headers and the keys and the values are the responses
    column = 0
    for value in row:
        response[headers[column]] = value
        column += 1
    responses.append(response)

# Print a frequecny table
question_to_view = "ethnicity"
print(pd.Series([response[question_to_view] for response in responses]).value_counts())
