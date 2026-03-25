
student = {
    "Name" : ["Ram","Sham","Anil","Sunil"],
    "Age" : [25,25,37,26],
    "Maths" : [98,87,76,58]
}
print(student)
student["Grade"] = ["A","B","C","D"]
print(student["Age"])

for key, value in student.items():
    print(key,":", value)


# person = {
#     "Name" : "Sangeet",
#     "Age" : 25,
#     "Company" : "SEDEMAC"
# } 
# print(person)