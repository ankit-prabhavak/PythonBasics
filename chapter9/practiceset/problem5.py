#Problem statement: Write a program to update and replace words of list in a file

words=["Donkey","gande","idiot"]


with open("file.txt","r") as f:
    content=f.read()
    for word in words:
      content=content.replace(word, "*"*len(word))

with open("file.txt","w") as f:
    f.write(content)


 