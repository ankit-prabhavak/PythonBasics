#Problem statement: Write a program to read a file and find a given word is present or not.
word=input("Enter the word: ")
with open("senorita.txt") as f:
    content=f.read()
    if word in content:
        print(f"{word} is present.")
    else:
        print(f"{word} is not present.")