# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input value for the rolled number
    X = int(input())
    
    # Check if Chef can enter a new token into the play
    if X == 6:
        print("YES")
    else:
        print("NO")
