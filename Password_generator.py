import random

print("""🌟 Welcome to PassWord Generator! 🌟

Hello,

Congratulations on taking the first step towards enhancing your online security! 
We're thrilled to welcome you to PassWord Generator!, 
your go-to destination for creating unique passwords.""")

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(" ")
amount_alpha = int(input("How many letters would you like to Add: "))
amount_numbers = int(input("How many numbers would you like to Add: "))
amount_symbols = int(input("How many symbols would you like to Add: "))

user_list = []

for _ in range(amount_alpha):
    user_list.append(random.choice(alphabets))

for _ in range(amount_symbols):
    user_list.append(random.choice(symbols))

for _ in range(amount_numbers):
    user_list.append(random.choice(numbers))

random.shuffle(user_list)

password = "".join(user_list)
print(f"Your PassWord is: {password}")
