def binomial_coefficient(n, k):
    # Create a 2D array to store the binomial coefficients
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate binomial coefficients in a bottom-up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base case: C(n, 0) = 1
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                # Recursive relation: C(n, k) = C(n-1, k-1) + C(n-1, k)
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]  # Return the binomial coefficient C(n, k)

# Input from the user
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    k = int(input("Enter the value of k: "))

    if k > n or k < 0:
        print("Invalid input: k must be between 0 and n.")
    else:
        result = binomial_coefficient(n, k)
        print(f"The binomial coefficient C({n}, {k}) is: {result}")
