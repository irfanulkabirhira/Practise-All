def solve():
    t = int(input())  # number of test cases
    for _ in range(t):
        n, k, q = map(int, input().split())  # n: length of array, k: consecutive subarray length, q: number of queries
        a = list(map(int, input().split()))  # array a
        
        # We will prepare a helper table to track where consecutive subarrays are possible
        possible = [0] * n
        
        # To make the subarray consecutive of length `k`, the differences should follow a specific pattern
        for i in range(n - k + 1):
            is_consecutive = True
            for j in range(i + 1, i + k):
                if a[j] != a[j - 1] + 1:
                    is_consecutive = False
                    break
            if is_consecutive:
                possible[i] = 1
        
        # Prepare a prefix sum of `possible` to help answer queries efficiently
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + possible[i - 1]
        
        # Now we answer the queries
        for _ in range(q):
            l, r = map(int, input().split())
            l -= 1
            r -= 1
            
            # We are interested in the range [l, r-k+1]
            if r - l + 1 < k:
                print(0)
            else:
                result = prefix_sum[r - k + 2] - prefix_sum[l]
                print(result)

# Reading input and running the solve function
if __name__ == "__main__":
    solve()
