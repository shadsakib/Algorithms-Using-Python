board = [[0 for x in range(100)] for y in range(100)]

def isSafe(row, col):

   for i in range(row, -1, -1):
       if board[i][col] == 1:
           return False

   for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
       if board[i][j] == 1:
           return False

   for i, j in zip(range(row, -1, -1), range(col, n)):
       if board[i][j] == 1:
           return False

   return True

def placeQueens(row):

    if row>=n: return True

    for i in range(n):

        if isSafe(row, i):
          board[row][i] = 1

          if placeQueens(row+1):
              return True
          else:
              board[row][i] = 0

    return False

n = int(input("Enter number of queens: "))
placeQueens(0)
for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()