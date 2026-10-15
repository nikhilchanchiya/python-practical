#calculate employee bonus
basic_salary= float(input("enter basic salary: "))
years = int(input("enter number of service: "))
if years <2:
    bonus = basic_salary * 5/100
elif years ==5:
    bonus = basic_salary * 10/100
elif years ==10:
    bonus = basic_salary * 15/100
else:
    bonus = basic_salary * 20/100
    gross_salary = basic_salary + bonus
    print("basic salary=",basic_salary)
    print("bonus=",bonus)
    print("gross salary=",gross_salary)