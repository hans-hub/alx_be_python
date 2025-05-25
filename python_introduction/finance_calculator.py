monthly_allowance = int(input("Enter you total monthly expenses: "))
monthly_expenses = int(input("Enter total monthly expenses: "))
monthly_savings = monthly_allowance - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", "$", projected_savings)
