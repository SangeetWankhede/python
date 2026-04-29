
def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i%2 == 0:
            print(i)
            count +=1
    return(count)
result = count_even(10)
print(result)   

def check_marks(marks):
    if marks >= 40 :
        return "Pass"
    else :
        return "Fail"
mark = float (input("Enter a marks: "))
result = check_marks(mark)
print(result)

