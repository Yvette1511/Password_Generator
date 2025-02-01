import random
import string

# sets of data
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

password_length = int(input("How many characters would you like in your password? "))

# checks password length

while True:
    if password_length < 8:
        print("Your password should be at least 8 characters long.")
        password_length = int(input("How many characters would you like in your password? "))
    else:
        break

# shuffles the data
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

result = []

# a % of the characters will be letters (part 1) and the rest will be special characters (part 2)
part1 = round(password_length * (30/100))
part2 = round(password_length * (20/100))

# password creation
for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

# reshuffles and prints the result
random.shuffle(result)

password = "".join(result)
print("Password - " + password)
