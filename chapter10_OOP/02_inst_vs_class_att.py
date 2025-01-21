class employee:
   #class attributes
    language="Hindi"
    salary="5000"

Ankit=employee()

Ankit.name="Ankit Kumar"  #instance or object attribute
Ankit.language="javascript"      #instance attribute take preference over class attribute.

print(Ankit.name,Ankit.language,Ankit.salary)

Aryan=employee()

Aryan.name="Aryan Ojha"    #instance or object attribute
Aryan.language="python"         #instance attribute take preference over class attribute.

print(Aryan.name,Aryan.language,Aryan.salary)

#Here name is objet attribute.language and salary are class attributes as they directly belong to the class. 