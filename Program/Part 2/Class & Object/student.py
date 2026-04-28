
class Student :
    #blueprint
    def __init__(self,name,email,id):
        self.name = name
        self.email = email
        self.id = id
        
s2 = Student("Sangeet","sangeet@gmail",1)
s1 = Student("Root","root@gmail",0)

print(s1.name)
print(s1.email)
print(s1.id)
print(" ")
print(s2.name)
print(s2.email)
print(s2.id)
