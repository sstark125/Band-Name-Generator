import os
def ConsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')


ConsoleClear()

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city = input("What City did you grow up in:\n")
#3. Ask the user for the name of a pet.
pet = input("What is the name of a pet:\n")
#4. Combine the name of their city and pet and show them their band name.
band = city + " " + pet
print("Your band name could be: " + band + "\n")
#5. Make sure the input cursor shows on a new line: