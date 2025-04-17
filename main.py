def longest_subsequence(seq, increasing=True):
    n = len(seq)
    dp = [1] * n
    prev = [-1] * n

    # Build the DP table
    for i in range(n):
        for j in range(i):
            if (increasing and seq[j] < seq[i]) or (not increasing and seq[j] > seq[i]):
                if dp[j] + 1 > dp [i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    # Find index of max length
    max_index = max(range(n), key=lambda i: dp[i])

    # Reconstruct the subsequence
    result = []
    while max_index != -1:
        result.append(seq[max_index])
        max_index = prev[max_index]
    return result[::-1]

# Input
n = 5
pi = [5, 1, 4, 2, 3]

# Get LIS and LDS
lis = longest_subsequence(pi, increasing=True)
lds = longest_subsequence(pi, increasing=False)

# Output
print("".join(map(str, lis)))
print("".join(map(str, lds)))
