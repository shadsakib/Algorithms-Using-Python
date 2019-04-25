money = int(input("Enter price: "))

coins = [2, 3, 4]

dp = [[0 for y in range(100)] for x in range(100)]

def coinChange():

    for i in range(1, money+1):
        dp[0][i] = i

    for i in range(1, len(coins)+1, 1):
        for j in range(1, money+1):
            if coins[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])


    return dp[len(coins)][money]

print("Minimum coins required:", end=" ")
print(coinChange())


