
class Employee :
    def __init__(self, role , dept , salary):
        self.role = role
        self.salary = salary
        self.dept = dept

    def showDetails(self):
        # print(self.role,self.dept,self.salary)
        print("Role is = ",self.role)
        print("Dept from = ",self.dept)
        print("Salary is = ",self.salary)

        
emp = Employee("Engg","IT","35000")
# emp.showDetails()

class Engineer(Employee):

    def __init__(self, name, age,):
        self.name = name
        self.age = age
        super().__init__("Accontant","Finnace","45000")
        
eng = Engineer("Sangeet",25)
print(eng.name,eng.age)
eng.showDetails()