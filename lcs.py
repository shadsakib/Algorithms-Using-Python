dp = [[0 for x in range(100)] for y in range(100)]
string = [["" for x in range(100)] for y in range(100)]
def computeLCS(x, y):

    for i in range(0, len(x)+1):
        dp[0][i] = 0

    for i in range(0, len(y)+1):
        dp[i][0] = 0

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                string[i][j] = "d"
            elif dp[i - 1][j] == dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                string[i][j] = "-|"
            elif dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                string[i][j] = "^"
            else:
                dp[i][j] = dp[i][j-1]
                string[i][j] = "<-"
            '''
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            '''

    return dp[len(x)][len(y)]

x, y = input("Enter two strings: ").split()
temp = computeLCS(x, y)

def printLCS(x, y, a, b, lcs):

    if a == -1 or b==-1:
        if len(lcs) == temp:
            print(lcs)
        print("kkk", lcs)
        return

    if string[a][b]=="d":
        lcs = x[a-1]+lcs
        print(lcs)
        printLCS(x, y, a-1, b-1, lcs)
    elif string[a][b] == "-|":
        printLCS(x, y, a - 1, b, lcs)
        printLCS(x, y, a, b - 1, lcs)
    elif string[a][b]=="^":
        printLCS(x, y, a-1, b, lcs)
    elif string[a][b]=="<-":
        printLCS(x, y, a, b-1, lcs)


print("Length of LCS = ", end=" ")
print(temp)
printLCS(x, y, len(x), len(y), "")