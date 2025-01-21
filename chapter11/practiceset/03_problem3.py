class Employee:
      salary=89556
      increment=22
      @property
      def salaryAfterincrement(self):
            return (self.salary + self.salary*(self.increment/100))
      
      @salaryAfterincrement.setter
      def salaryAfterincrement(self, salary):
            self.increment = ((salary/self.salary)-1)*100
            



e=Employee()
print(e.salaryAfterincrement)

e.salaryAfterincrement=100000
print(e.salaryAfterincrement)
print(e.increment)
