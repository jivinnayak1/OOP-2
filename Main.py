class Employee:
    def __init__(self,Name,ID,Age,Salary=30000):
        self.Name = Name
        self.ID = ID
        self.Age = Age
        self.Salary = Salary
    def Details(self):
        print(f"Employee Name: {self.Name}\nEmployee ID: {self.ID}\nEmployee Age {self.Age}\nEmployee Salary: {self.Salary}")
    def Wish(self):
        print("Hello")



emp1 = Employee("Jivin",1234,25)
emp2 = Employee("Suman",2345,26)

print(emp1.Details())
print(emp2.Wish())