monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
interest = 0.05
yearly_savings = monthly_savings * 12 + (monthly_savings * 12 * interest)

print("Projected savings after one year, with interest, is: ＄", yearly_savings)