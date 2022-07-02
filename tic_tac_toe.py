pos_count = []


def checkBoard(r, c):
    if not ((r == 1 and c == 2) or (r == 1 and c == 2) or (r == 2 and c == 3) or (r == 3 and c == 2)):
        if board[0][0] == board[1][1] == board[2][2]:
            return True
        elif board[0][2] == board[1][1] == board[2][0]:
            return True
    if board[r - 1][0] == board[r - 1][1] == board[r - 1][2]:
        return True
    elif board[0][c - 1] == board[1][c - 1] == board[2][c - 1]:
        return True


def printBoard():
    for row in range(len(board)):
        print("--   --  --")
        for col in range(len(board[row])):
            if col % 2 == 1:
                print(f" {board[row][col]}", end="")
            else:
                print(f"| {board[row][col]} |", end="")
        print()


def placeCharacter(pos, char, board):
    # global board
    r = 0
    pos = int(pos)
    c = 0
    if pos in pos_count:
        print("change your value and face penalty")
    else:
        pos_count.append(pos)
        if pos == 1:
            board[0][0] = char
            r = 1
            c = 1

        elif pos == 2:
            board[0][1] = char
            r = 1
            c = 2

        elif pos == 3:
            board[0][2] = char
            r = 1
            c = 3

        elif pos == 4:
            board[1][0] = char
            r = 2
            c = 1

        elif pos == 5:
            board[1][1] = char
            r = 2
            c = 2

        if pos == 6:
            board[1][2] = char
            r = 2
            c = 3

        elif pos == 7:
            board[2][0] = char
            r = 3
            c = 1

        if pos == 8:
            board[2][1] = char
            r = 3
            c = 2

        if pos == 9:
            board[2][2] = char
            r = 3
            c = 3
        pos_count.append(pos)
        return checkBoard(r, c)


def gameInitialization():
    global player1, player2
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    print(f"{player1}, your character is X")
    print(f"{player2}, your character is O")


def runGame():
    counter = 0
    f = False
    p_name = None
    while counter < 9:
        printBoard()
        if counter % 2 == 0:
            if placeCharacter(input(f"{player1}, where do you want to place 'X': "), 'X', board):
                p_name = player1
                f = True
                break
        else:
            if placeCharacter(input(f"{player2}, where do you want to place 'O': "), 'O', board):
                p_name = player2
                f = True
                break
        counter += 1
    printBoard()

    if f:
        print(f'{p_name} won')
    else:
        print("Draw")


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
player1 = player2 = None
gameInitialization()
runGame()
