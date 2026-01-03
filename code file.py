#calculating monthly payment using loan formula
name = input("Enter your name: ")
loans = []

while True:
    # inputs
    p = float(input("What's the principal amount? = "))
    a = float(input("What's the annual interest rate (%)? = "))
    b = float(input("The term (in years) = "))

    # conversions
    i = a / 1200          
    n = int(b * 12)       

    
    emi = p * i * (1 + i) ** n / ((1 + i) ** n - 1)

    if emi < 0:
        print("Something went wrong, enter your values again.")
    else:
        print(name)
        print(emi, "is your monthly loan payment or EMI")

        loan_info = {
            "name": name,
            "principal": p,
            "rate": a,
            "months": n,
            "emi": emi
        }
        loans.append(loan_info)

        print(f"{name} EMI: {emi:.2f}")

    more = input("Add another loan? (y/n): ").lower().strip()
    if more != 'y':
        break

print("\nAll loans:")
for loan in loans:
    print(f"{loan['name']}: EMI={loan['emi']:.2f}")

x = input("do you want to know the total interest amount you will be paying? (y/n): ")
if x == 'y':
    print((emi*12*b)-p,"is the total interest amount you will be paying")
else:print("\nAll loans:")
for loan in loans:
    print(f"{loan['name']}: EMI={loan['emi']:.2f}")

