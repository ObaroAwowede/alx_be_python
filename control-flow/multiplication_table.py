number = int(input("Enter a number to see its multiplication table:"))

for i in range(1,10):
    ans = i * number
    print(number, "*", i ," = ", ans)