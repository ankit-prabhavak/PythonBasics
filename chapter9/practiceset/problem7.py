import string

with open("senorita.txt", "r", encoding="utf-8") as f:
    line = f.read()

count = 0
for word in line.split():
    word = word.lower().strip(string.punctuation)  # This will remove any surrounding punctuation
    if word == "señorita":
        count += 1

print("señorita appears", count, "times in the file.")
