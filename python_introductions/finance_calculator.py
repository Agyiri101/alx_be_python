monthly_income = input("Enter your monthly income : ")
monthly_expenses = input("Enter you total monthly expenses")
monthly_income = float(monthly_income)
monthly_expenses = float(monthly_expenses)
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
projected_savings =annual_savings + (annual_savings * 0.05)
print(f"your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is : ${projected_savings}")
