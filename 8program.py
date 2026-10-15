print("----percentage calculation----")
marks1 = int(input("enter marks for  student1: "))
marks2 = int(input("enter marks for  student2: "))
marks3 = int(input("enter marks for  student3: "))

total = marks1 + marks2 + marks3
percentage = total/3

if percentage > 90:
    grade = "O"
elif percentage > 80:
    grade = "A"
elif percentage > 70:
    grade = "B"
elif percentage > 60:
    grade = "C"
elif percentage > 50:
    grade = "D"
elif percentage > 40:
    grade = "E"
elif percentage < 40:
    grade = "F"

print("="*25)
print("subject1 =",marks1)
print("subject2 =",marks2)
print("subject3 =",marks3)
print("total =",total)
print("percentage ={:.2f}%",format(percentage))
print("grade =",grade)
print("="*25)