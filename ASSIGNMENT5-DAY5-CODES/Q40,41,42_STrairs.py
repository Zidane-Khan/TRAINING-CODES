def countWays(n):
    if n == 0 or n == 1:
        return 1

    # dp array to store the number of ways to reach each step
    dp = [0] * (n + 1)
    
    # There is 1 way to reach the 0th step (stay there)
    dp[0] = 1

    # There is 1 way to reach the 1st step (take one step)
    dp[1] = 1

    # Fill the dp array for steps from 2 to n
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # The number of ways to reach step i

    return dp[n]  # Return the number of ways to reach the nth step

n = 5
print(f"The number of ways to reach the top of {n} stairs is: {countWays(n)}")
