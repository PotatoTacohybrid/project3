import random

with open("garfield.txt", "r") as file:
    garfieldWords = file.read().splitlines()

output = ""

for i in range(int(input("length of garfield: "))):
    output += garfieldWords[random.randint(0, len(garfieldWords) - 1)] + " "

print(output)