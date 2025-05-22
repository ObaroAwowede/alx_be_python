monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
interest = 0.05
yearlysaving = savings * 12 + (savings * 12 * interest)

print("Projected savings after one year, with interest, is: ＄", yearlysaving)