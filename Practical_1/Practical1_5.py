#5. Python program to solve quadratic Equation
a=int(input("Enter coeff of x^2"))
b=int(input("Enter coeff of x"))
c=int(input("Enter the remaining constant"))
eq=(b**2-4*a*c)**0.5
r1=(-b-eq)/2*a
r2=(-b+eq)/2*a
print(r1,r2)