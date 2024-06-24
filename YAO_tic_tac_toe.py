def tic_tac_toe(board):
    vertical = []
    vertical_winner = ""
    horizontal_winner =""
    diagonal = []
    backdiagonal= []
    diagonal_winner = ""
    final_winner =""

    #arrangement
    
    #vertical string
    for i in range (0,len(board)):
        for j in range (0, len(board)):
            if board[i][j] =='':
                vertical += "E"
            else:
                vertical += board[i][j]
    
    #diagonal string
    for m in range (0, len(board)):
        for n in range (0, len(board)):
            if m == n:
                diagonal_letter = board[m][n]
                diagonal += diagonal_letter
    for w in range (0,len(board)):
        for q in range ((-(len(board))),0):
            if w == (-(q+1)):
                diagonal_letter_back = board[w][q]
                backdiagonal += diagonal_letter_back
    
    # Start of the winner finding
    
    #vertical winner
    for k in range (0,len(board)):
        if vertical[k::len(board)].count('X') == len(board):
            vertical_winner += "X"
        elif vertical[k::len(board)].count('O') ==len(board):
            vertical_winner += "O"
        else:
            vertical_winner +=""
    
    #horizontal winner
    for l in range (0,len(board)):
        if board[l].count('X')==len(board):
            horizontal_winner += "X"
        elif board[l].count('O')==len(board):
            horizontal_winner += "O"
        else:
            horizontal_winner +=""

    #diagonal winner
    if diagonal.count('X')== len(board):
        diagonal_winner = "X"
    elif diagonal.count('O') == len(board):
        diagonal_winner = "O"
    else: 
        if backdiagonal.count('X')== len(board):
            diagonal_winner = "X"
        elif backdiagonal.count('O') == len(board):
            diagonal_winner = "O"
        else:
            diagonal_winner = ""

    if vertical_winner == "X":
        final_winner += "X"
    elif vertical_winner == "O":
        final_winner += "O"
    elif horizontal_winner =="X":
        final_winner += "X"
    elif horizontal_winner =="O":
        final_winner+="O"
    elif diagonal_winner =="X":
        final_winner+= "X"
    elif diagonal_winner == "O":
        final_winner+= "O"
    else: 
        final_winner = "NO WINNER"

    return final_winner