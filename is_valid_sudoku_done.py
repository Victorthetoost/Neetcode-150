class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows no dupes
        #columns no dupes
        #3x3 no dupes

        #rows
        for i in range(0,len(board[0])):
            appeared_nums = []
            #goes row by row, column by column checking for dupes
            for j in range(0,len(board)):
                if board[j][i] != ".":
                    if board[j][i] in appeared_nums:
                        return False
                    else:
                        appeared_nums.append(board[j][i])
        #columns same as rows but switched
        for j in range(0,len(board[0])):
            appeared_nums = []
            for i in range(0,len(board)):
                if board[j][i] != ".":
                    if board[j][i] in appeared_nums:
                        return False
                    else:
                        appeared_nums.append(board[j][i])
        # there are 3 boxes in the row and 3 boxes in the column
        for row in range(0,3):
            for col in range(0,3):
                start_row = 3*row
                start_col = 3*col
                appeared_nums = []
                for i in range(start_row,start_row+3):
                    for j in range(start_col,start_col+3):
                        if board[j][i] != ".":
                            if board[j][i] in appeared_nums:
                                return False
                            else:
                                appeared_nums.append(board[j][i])   
        return True