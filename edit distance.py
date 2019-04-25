dp = [[0 for x in range(100)] for y in range(100)]

def editDistance(x, y):

    for i in range(1, len(x)+1):
        dp[0][i] = i

    for i in range(1, len(y)+1):
        dp[i][0] = i

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j], dp[i ][j-1], dp[i-1][j-1])

    return dp[len(x)][len(y)]

x, y = input("Enter two strings: ").split(" ")

print("Minimum operations: ", editDistance(x, y))