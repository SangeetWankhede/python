
class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def avg_marks(self) :
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your avg marks is:",sum/3)
          
      
s1 = Student("Ironman",[98,97,99])  
s1.avg_marks()  

s2 = Student("Tony",[99,99,99])
s2.avg_marks()