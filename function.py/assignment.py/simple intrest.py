def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
1
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the annual interest rate : "))
time = int(input("Enter the time period : "))

interest = calculate_simple_interest(principal, rate, time)
print("Simple interest:", interest)

