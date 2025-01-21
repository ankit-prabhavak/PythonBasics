#Problem statement: update and replace in file.


word="bye"

with open("file.txt","r") as f:
    content=f.read()

    contentnew=content.replace(word, "***")

with open("file.txt","w") as f:
    f.write(contentnew)


 