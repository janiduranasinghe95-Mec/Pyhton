name = input("Enter your name: ")
basic_salary = float(input("Enter your basic salary: "))
Monthly_allowance = float(input("Enter your monthly allowance: "))
performance_bonus = float(input("Enter your performance bonus: "))

if basic_salary < 0 or Monthly_allowance < 0 or performance_bonus < 0:
    print("Entered Employee name :", name)
    print("Entered basic salary : Rs.", basic_salary)
    print("Entered monthly allowance : Rs.", Monthly_allowance)
    print("Entered performance bonus : Rs.", performance_bonus)
    print()
    print("Invalid input.")
    print("Salary, allowance and bonus cannot be negative.")

else:
    if basic_salary < 75000:
        tax_rate = 0 / 100
    elif basic_salary < 100000:
        tax_rate = 5 / 100
    elif basic_salary < 150000:
        tax_rate = 10 / 100
    else:
        tax_rate = 15 / 100

    gross_salary = basic_salary + Monthly_allowance + performance_bonus
    Tax = gross_salary * tax_rate
    net_salary = gross_salary - Tax

    Executive_per = "Yes" if gross_salary >= 150000 else "No"
    Annual_Incentive = "Yes" if net_salary >= 120000 else "No"
    Performer_recognition = "Yes" if performance_bonus >= 25000 else "No"

    print()
    print("Employee name :", name)
    print("Gross Salary : Rs.", gross_salary)
    print("Income Tax : Rs.", Tax)
    print("Net Salary : Rs.", net_salary)
    print()
    print("Executive performance bonus :", Executive_per)
    print("Eligible for Annual Incentive :", Annual_Incentive)
    print("Performance Bonus :", performance_bonus)