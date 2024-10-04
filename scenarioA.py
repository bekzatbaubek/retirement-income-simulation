import matplotlib.pyplot as plt

# Initial information
retirement_savings = 100000
salary = 20000
savings_as_proportion_of_wage = 10
age = 30
retirement_age = 70

# Create an empty list of savings that we will fill in for each ear
savings_each_year = []
# Simulation: repeat for each year from your current age to retirement
for year in range(age, retirement_age):
    retirement_savings *=  1.02
    # savings_as_proportion_of_wage / 100.0 will help us convert human-readable percentage (i.e. 3 is 3%)
    # to its actual value (i.e. 0.03)
    retirement_savings += (salary * savings_as_proportion_of_wage / 100.0) * 12
    salary *= 1.02
    # Append the calculated retirement savings value to the list
    savings_each_year.append(retirement_savings)

# Plotting the savings for each year
plt.title("Savings growth in an ideal scenario")
plt.xlabel("Age")
plt.ylabel("Savings amount")
plt.ticklabel_format(style='plain')
plt.plot(range(age, retirement_age), savings_each_year)
plt.show()

# Output the result of the simulation to the command line
print(f"[Scenario A] When you retire at {retirement_age}, you will have {retirement_savings:.2f} in your bank account")