# calculate gross salary

basis_salary= float(input("enter basis salary"))
if basis_salary <= 1000:
    hra = basis_salary * 20/100
    da = basis_salary *80/100

elif basis_salary <= 2000:
    hra= basis_salary*25/100
    da= basis_salary *90/100
else:
    hra= basis_salary*30/100
    da= basis_salary *95/100
gross_salary =basis_salary+hra+da
print("HRA :=",hra)
print("DA :=",da)
print("gross salary=",gross_salary)