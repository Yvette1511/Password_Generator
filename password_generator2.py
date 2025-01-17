import random
import time

lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","d","u","v","w","x","y","z"]
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!","?","@","/","#","*"]
password = ""

char_options = ["1","2","3","4"]

time.sleep(0.5)
print("Welcome to the password generator!")
time.sleep(1)
password_char = int(input("How many characters would you like in your password? "))

for num in range (0, password_char):
    char_choice = random.choice(char_options)
    if char_choice == "1":
        password += random.choice(lower)
    elif char_choice == "2":
        password += random.choice(upper)
    elif char_choice == "3":
        password += random.choice(numbers)
    else:
        password += random.choice(special)

print(password)


