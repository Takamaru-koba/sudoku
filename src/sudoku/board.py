def print_board(board):
    
    if len(board) != 9:
        raise ValueError
    
    for row in board:
        if len(row) != 9:
            raise ValueError

    for i in range(9):
        k = 0
        print()
        if i % 3 == 0 and i != 0:
            for j in range(2):
                print("-"*6 + "+", end=" ")
            print("-"*6)
        for l in range(9):
            print(board[i][k], end=" ")
            k += 1
            if k == 3 or k == 6:
                print("|", end=" ")
    print()


