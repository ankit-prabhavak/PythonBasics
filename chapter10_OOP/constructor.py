class employee:
   #class attributes
    language="Hindi"
    salary="5000"

    def __init__(self,name,language,salary):   #it is a dunder method which is automatically called.
        self.name=name
        self.language=language
        self.salary=salary  
        print("I am creating an object.")


    def getinfo(self):
        
        print(f"Language is: {self.language}. The salary is: {self.salary}.")
    
    @staticmethod     
    def greet():
        print("Good morning sir!")



Ankit=employee("Kumar","Python",5000)

Ankit.name="Ankit Kumar"  
Ankit.language="javascript"      

Ankit.greet()
Ankit.getinfo()
print(Ankit.name,Ankit.language,Ankit.salary)
