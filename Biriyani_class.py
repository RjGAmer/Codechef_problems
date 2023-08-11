# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input values for weeks and cost per week
    X, Y = map(int, input().split())
    
    # Calculate the total amount Chef has to pay
    total_payment = X * Y
    
    # Print the total payment for this test case
    print(total_payment)
