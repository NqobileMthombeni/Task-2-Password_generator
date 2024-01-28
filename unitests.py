import unittest
from unittest.mock import patch
import random

def generate_password(amount_alpha, amount_numbers, amount_symbols):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    user_list = []

    for _ in range(amount_alpha):
        user_list.append(random.choice(alphabets))

    for _ in range(amount_symbols):
        user_list.append(random.choice(symbols))

    for _ in range(amount_numbers):
        user_list.append(random.choice(numbers))

    random.shuffle(user_list)

    password = "".join(user_list)
    return password

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password(self):
        # Test with specific values for the number of letters, numbers, and symbols
        password = generate_password(4, 3, 2)

        # Check if the generated password length is correct
        self.assertEqual(len(password), 9)  # 4 letters + 3 numbers + 2 symbols = 9 characters

        # Check if there are at least 4 letters
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(sum(char.isalpha() for char in password) >= 4)

        # Check if there are at least 3 numbers
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(sum(char.isdigit() for char in password) >= 3)

        # Check if there are at least 2 symbols
        self.assertTrue(any(char in '!@#$%^&*()_+-={}[]|\\:;"\'<>,.?/' for char in password))
        self.assertTrue(sum(char in '!@#$%^&*()_+-={}[]|\\:;"\'<>,.?/' for char in password) >= 2)

if __name__ == '__main__':
    unittest.main()
