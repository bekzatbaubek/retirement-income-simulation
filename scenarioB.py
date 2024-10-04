import matplotlib.pyplot as plt
import random

retirement_savings = 100000
salary = 20000
savings_as_proportion_of_wage = 20
age = 30
retirement_age = 70

savings_each_year = []
for year in range(age, retirement_age):
    retirement_savings = retirement_savings * 1.02
    # Roll an imaginary 100-sided die
    dice = random.randint(1, 100)
    # A chance of rolling a number equal to or less than 10 (out of a 100) is 10%
    if dice <= 10:
        # Calculate spending for that year:
        # calculate the proportion of the income that is spent - remaining income after savings
        spending_this_year = ((100 - savings_as_proportion_of_wage) / 100.0) * salary * 12
        retirement_savings -= spending_this_year
        # Salary reduction anywhere from 0% to 100%
        salary = salary * random.random()
    else:
        salary = salary * 1.02
        retirement_savings += (salary * savings_as_proportion_of_wage / 100.0) * 12

    savings_each_year.insert(year, retirement_savings)

plt.title("Savings growth in a realistic scenario")
plt.xlabel("Age")
plt.ylabel("Savings amount")
plt.ticklabel_format(style='plain')
plt.plot(range(age, retirement_age), savings_each_year)
plt.show()

print(f"[Scenario B] When you retire at {retirement_age}, you will have {retirement_savings:.2f} in your bank account")