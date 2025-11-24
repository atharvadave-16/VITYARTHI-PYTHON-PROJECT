#calculating monthly payment using loan formula
p = float(input("whats the principal amount = "))
i = float(input("whats the monthly intrest rate = "))
n = float(input("the term (in months) = "))
m = p*((i*(i+1)**n)/(((1+i)**n) - 1))
if m < 0:
    print("enter your values again")
else:
    print(m ," is your monthly loan payment")