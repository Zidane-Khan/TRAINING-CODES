def coinChangeWays(amount, coins):

    dp = [0] * (amount + 1)
    dp[0] = 1  
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]  
    
    return dp[amount]

amount = 5
coins = [1, 2, 5]
print(coinChangeWays(amount, coins)) 
