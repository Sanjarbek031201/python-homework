1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
from datetime import date

# Get current year
current_year = date.today().year

# Ask for user input
name = input("What is your name? ")
birth_year = input("What year were you born? ")

# Validate and calculate age
try:
    birth_year = int(birth_year)
    age = current_year - birth_year

    # Display result
    print(f"Hello, {name}! You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")
2. Extract Car Names
Extract car names from the following text:
# List of sample car names
car_names = ['Ford', 'Toyota', 'BMW', 'Honda', 'Tesla', 'Audi', 'Lexus', 'Mazda', 'Nissan', 'Chevrolet', 'Subaru', 'Kia']
# Input text
txt = 'LMaasleitbtui'.lower()
# Search for car names in the text
found_cars = [car for car in car_names if car.lower() in txt]
print("Car names found:", found_cars)
txt = 'LMaasleitbtui'
3. Extract Car Names
Extract car names from the following text:
def extract_car_names(txt):
    car_brands = ['Ford', 'Toyota', 'BMW', 'Honda', 'Tesla', 'Audi', 'Lexus', 
                  'Mazda', 'Nissan', 'Chevrolet', 'Subaru', 'Kia', 'Jeep', 'Dodge']
  found = []
    lower_txt = txt.lower()
    for brand in car_brands:
        if brand.lower() in lower_txt:
            found.append(brand)
    
    return found

txt = 'MsaatmiazD'
result = extract_car_names(txt)
print("Car names found:", result)
txt = 'MsaatmiazD'
4. Extract Residence Area
Extract the residence area from the following text:
import re

txt = "I'am John. I am from London"

# Regular expression to find location after "I am from" or similar patterns
match = re.search(r'\bI\s*(?:am|'m)\s*from\s+([A-Za-z\s]+)', txt, re.IGNORECASE)

if match:
    residence = match.group(1).strip()
    print("Residence area found:", residence)
else:
    print("No residence area found.")
txt = "I'am John. I am from London"
5. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.
# Ask for user input
user_input = input("Enter a string: ")

# Reverse the string using slicing
reversed_string = user_input[::-1]

# Display the reversed string
print("Reversed string:", reversed_string)
6. Count Vowels
Write a Python program that counts the number of vowels in a given string.
# Get user input
text = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
vowel_count = sum(1 for char in text if char in vowels)

# Display the result
print("Number of vowels:", vowel_count)
7. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.
# Ask the user to enter numbers separated by spaces
numbers_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, numbers_input.split()))

# Find the maximum value
max_value = max(numbers)

# Print the maximum value
print("The maximum value is:", max_value)
8. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
# Get user input
word = input("Enter a word: ")

# Normalize the word to lowercase to make the check case-insensitive
normalized_word = word.lower()

# Check if the word reads the same forward and backward
if normalized_word == normalized_word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
9. Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.
# Get user input
email = input("Enter your email address: ")

# Split the email at '@' and get the domain part
if '@' in email:
    domain = email.split('@')[1]
    print("Domain:", domain)
else:
    print("Invalid email address! No '@' symbol found.")
10. Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4 for good security.")
        return None

    # Characters to choose from
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # Special characters like !@#$%

    # Ensure the password has at least one letter, one digit, and one special char
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the rest of the password length with a mix of all character types
    all_chars = letters + digits + special_chars
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the password list to randomize character positions
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Example usage
password = generate_password(12)
print("Generated password:", password)
