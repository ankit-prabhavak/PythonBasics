s="my name is ankit."


# z=s.capitalize()
# print(s)
# print(z)


# x=s.casefold()
# print(s)
# print(x)


# name="ankit"
# n=name.capitalize()

# print(n.center(5,'-'))


# print(n.count('i'))



# s="k\to\tl\tk\tt\ta"
# print(s.expandtabs(4))

# s="ankit"

# print(s.lower())

# print(s.upper())


# s="my name is ankit"

# print(s.split())

# s="my-name-is-ankit"
# print(s.split())



# s="my name is ankit"

# print(s.title())

# print(s.swapcase())

# s="       ankit          "
# print(s.strip())

# print(s.lstrip())


# print(s.rstrip())

# s="my name is ankit"
# print(''.join(s))


# s='50'
# print(s.zfill(10))


# print(s.isdigit())


# s="kolaktai"

# print(s.find('i'))

# s="ian ainni kii"

# print(s.rfind('k'))


# print(s.index('a'))

# print(s.rindex('n'))

# s="my name is ankit"

# print(s.replace('name','naam'))


# s="my name is {}, i am {} year lod."

# print(s.format("ankit",18))



#lex_auth_012693816331657216161

def encode(message):
   text = ""   
   count = 0
   c = message[0] 

   for i in range(0,len(message)):
       if c == message[i]:
          count+=1
       else:
           text += str(count)
           text += message[i-1]
           c=message[i]   
           count=1

   text += str(count)
   text += c
   return text
#Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message) 