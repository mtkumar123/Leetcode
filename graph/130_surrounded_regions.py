from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited_nodes = set()
        def dfs(i, j):
            if (i,j) in visited_nodes:
                return
            visited_nodes.add((i,j))
            board[i][j] = "T"
            if i-1>=0 and board[i-1][j] == "O":
                dfs(i-1, j)
            if i+1<len(board) and board[i+1][j] == "O":
                dfs(i+1, j)
            if j-1>=0 and board[i][j-1] == "O":
                dfs(i, j-1)
            if j+1<len(board[i]) and board[i][j+1] == "O":
                dfs(i, j+1)

        for i in range(0, len(board)):
            if board[i][0] == "O" and (i,0) not in visited_nodes:
                dfs(i, 0)
            if board[i][-1] == "O" and (i,len(board[i])-1) not in visited_nodes:
                dfs(i, len(board[i])-1)  
            if i == 0 or i==len(board)-1:
                for j in range(1, len(board[i])-1):
                    if board[i][j] == "O" and (i, j) not in visited_nodes:
                        dfs(i, j) 

        for i in range(0, len(board)): # y axis
            for j in range(0, len(board[i])): # x axis
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board

s = Solution()
board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board2 = [["X"]]
board3 = [["X","O","X"],["X","O","X"],["X","O","X"]]

result = s.solve(board1)
result2 = s.solve(board2)
result3 = s.solve(board3)
print(result)
print(result2)
