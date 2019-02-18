bannedWords = input("Comma seperated words: ").split(",")


text = input("Text to censor: ").split()


output = ""

for i in range(len(text)):
    if text[i] in bannedWords:
        for x in range(len(text[i])):
            output += "*"
        output += " "
    else:
        output += text[i] + " "


with open("output.txt", "w") as file:
    file.write(output)



print(output)