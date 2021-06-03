file = open("data.csv", "r")
data = []
headers = []
responses = []
for line in file:
    data.append(line)
# Get the headers
for value in data[0].split(","):
    headers.append(value)
# Get the responses
for response in data[2::2]:
    response_list = {}
    count = 0
    for value in response.split(","):
        count += 1
        if count < 77:
            response_list[headers[count - 1]] = value
    responses.append(response_list)
for response in responses:
    print(response['age_range'])
# print(responses)