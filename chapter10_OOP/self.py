class employee:
   #class attributes
    language="Hindi"
    salary="5000"


    def getinfo(self):
        print(f"Language is: {self.language}. The salary is: {self.salary}.")
    
    @staticmethod     #it make the greet() to not take objet properties as we just need to print good morning.
    def greet():
        print("Good morning sir!")



Ankit=employee()

Ankit.name="Ankit Kumar"  #instance or object attribute
Ankit.language="javascript"      #instance attribute take preference over class attribute.

Ankit.greet()
Ankit.getinfo()
# employee.getinfo(Ankit)

Aryan=employee()

Aryan.name="Aryan Ojha"    #instance or object attribute
Aryan.language="python"         #instance attribute take preference over class attribute.

Aryan.greet()
Aryan.getinfo()
# employee.getinfo(Aryan)

#Here name is objet attribute.language and salary are class attributes as they directly belong to the class. 