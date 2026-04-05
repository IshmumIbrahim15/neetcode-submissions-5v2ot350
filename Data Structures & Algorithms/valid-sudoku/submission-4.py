class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                #check rows
                if board[i][j] in rows[i]:
                    print("row at", i, ": false")
                    print(rows[i])
                    return False
                else:
                    rows[i].add(board[i][j])

                #check columns
                if board[i][j] in cols[j]:
                    print("column at", j, ": false")
                    print(cols[j])
                    return False
                else:
                    cols[j].add(board[i][j])
                
                #check boxes
                if board[i][j] in square[int(i/3), int(j/3)]:
                    print("square at", i, j, ": false")
                    print(square[int(i/3), int(j/3)])
                    return False
                else:
                    square[int(i/3), int(j/3)].add(board[i][j])
            print("\n")
        
        print(square)
        return True

                
        