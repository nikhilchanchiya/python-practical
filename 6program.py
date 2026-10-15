#create a dictionary
student={
    "name":"rahul",
    "course":"mca",
    "semester":3,
    "marks":85
}

#1.print the dictionary items
print("ditionary:",student)

#2.Access items
print("student name:",student["name"])
print("student course:",student["course"])

#3. use get()
print("student semester:",student.get("semester"))
print("student marks:",student.get("marks"))

#4.change values
student["marks"]=90
student["semester"]=4

print("dictionary after changing values:",student)

#5. use len()
print("number of items:",len(student.items()))