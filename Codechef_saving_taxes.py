
T = int(input())


for _ in range(T):
    # Read the input values
    X, Y = map(int, input().split())
    
    # Calculate the minimum amount to invest
    min_investment = max(0, X - Y)
    
    # Print the result for this test case
    print(min_investment)