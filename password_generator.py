import random

# Take inputs
name = input("Enter your name: ")
date = input("Enter today's date (dd/mm/yyyy): ")
gmail = input("Enter your Gmail: ")

# Extract part of Gmail before @ (username part only)
gmail_user = gmail.split("@")[0]

# Concatenate all input data
data = name + date + gmail_user

# Characters pool (letters + numbers + symbols for stronger password)
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*?"

all_chars = lowercase + uppercase + digits + symbols

# Function to return a random character from given string
def get_random_char(source):
    return random.choice(source)

# Password length fixed (between 8 and 10 → here 9)
password_length = 9

# Ensure at least one char from each category + user data
password = [
    get_random_char(lowercase),
    get_random_char(uppercase),
    get_random_char(digits),
    get_random_char(symbols),
    get_random_char(data)   # ensures something from name/date/gmail
]

# Fill the rest until password_length = 9
while len(password) < password_length:
    if random.choice([True, False]):
        password.append(get_random_char(data))
    else:
        password.append(get_random_char(all_chars))

# Shuffle so order is random
random.shuffle(password)

# Join list into string
final_password = "".join(password)

print("Your generated password is:", final_password)
