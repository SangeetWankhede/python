student = {}

while True :
    print("\n ---- STUDENT MANAGER APP ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input ("Enter your choice: ")

# Add student data 
    if choice == "1" :
        name = input("Enter a student name: ")
        marks = int(input("Enter student marks: "))
        student [name] = marks
        print(f"{name} Successfully Added !!")

    #view student
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks,in student.item():
                print(name,":",marks)

    #check result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[marks]

            if marks > 40 :
                print("Pass")
            else:
                print("Fail")
        
    elif choice == "4":
            print("Exiting...!!")
            break

    else:
            print("In_valid input")