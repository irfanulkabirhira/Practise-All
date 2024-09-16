# Function to calculate alternating sum for each test case
def alternating_sum(nums):
    total = 0
    for i in range(len(nums)):
        if i % 2 == 0:  # If index is even, add the number (0-based index)
            total += nums[i]
        else:  # If index is odd, subtract the number
            total -= nums[i]
    return total

# Input: number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Length of the sequence
    nums = list(map(int, input().split()))  # The sequence of integers
    result = alternating_sum(nums)
    print(result)
