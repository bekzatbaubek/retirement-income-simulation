import matplotlib.pyplot as plt
import random

retirement_savings = 100000
salary = 20000
savings_as_proportion_of_wage = 10
investment_as_proportion_of_savings = 30
age = 30
retirement_age = 70

savings_each_year = []
for year in range(age, retirement_age):
    # Calculate investment returns
    # Random return - from losing 20% to gaining 20%
    profit_or_loss_percentage = random.randint(-20, 20)
    # Invest only if there are funds to invest
    if retirement_savings > 0:
        # Savings from investment: multiply the proportion of savings invested by the return percentage
        retirement_savings += (retirement_savings * investment_as_proportion_of_savings / 100.0) * profit_or_loss_percentage / 100.0

    retirement_savings = retirement_savings * 1.02

    dice = random.randint(1, 100)
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

plt.title("Savings growth in a dynamic scenario")
plt.xlabel("Age")
plt.ylabel("Savings amount")
plt.ticklabel_format(style='plain')
plt.plot(range(age, retirement_age), savings_each_year)
plt.show()

print(f"[Scenario C] When you retire at {retirement_age}, you will have {retirement_savings:.2f} in your bank account")