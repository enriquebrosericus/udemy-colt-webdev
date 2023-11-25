import random

# Define the Powerball numbers
powerball_numbers = [1, 2, 3, 4, 5, 6]

# Generate a random Powerball number
random_number = random.choice(powerball_numbers)
print(random_number)

# Create a list of tickets
tickets = []

# Generate tickets until the Powerball number is matched
while random_number not in tickets:
    ticket = random.sample(powerball_numbers, 6)
    tickets.append(ticket)
    print(ticket)

# Print the winning ticket
print(tickets[-1])
