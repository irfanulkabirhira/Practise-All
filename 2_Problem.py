def solve():
    t = input().strip()
    n = len(t)
    
    # Try all possible lengths of the original message s
    for length in range(1, n):
        s = t[:length]
        
        # Check if the message `t` can be formed by merging two identical `s`
        merged_message = s + t[length:]
        
        if merged_message == t:
            print("YES")
            print(s)
            return
    
    # If no valid s is found, print NO
    print("NO")

# Call the solve function to run the solution
solve()
