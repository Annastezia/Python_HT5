board = [1,2,3,
        4,5,6,
        7,8,9]
 
vic_lines = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
def print_board():
    print(board[0], end = " ")
    print(board[1], end = " ")
    print(board[2])
 
    print(board[3], end = " ")
    print(board[4], end = " ")
    print(board[5])
 
    print(board[6], end = " ")
    print(board[7], end = " ")
    print(board[8])    
 
# Сделать ход в ячейку
def move_board(move,symb):
    ind = board.index(move)
    board[ind] = symb
 
def get_result():
    vic = " "
 
    for i in vic_lines:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            vic = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            vic = "O"   
             
    return vic
 
game_over = False
player1 = True
 
while game_over == False:
 
    print_board()
 
    if player1 == True:
        symb = "X"
        move = int(input("Человек 1, ваш ход: "))
    else:
        symb = "O"
        move = int(input("Человек 2, ваш ход: "))
 
    move_board(move,symb) 
    vic = get_result() 
    if vic != " ":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
 
print_board()
print("Победил", vic)