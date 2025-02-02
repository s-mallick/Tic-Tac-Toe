row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def display(row1, row2, row3):
    print(f"{row1[0]}|{row1[1]}|{row1[2]}")
    print('------')
    print(f"{row2[0]}|{row2[1]}|{row2[2]}")
    print('------')
    print(f"{row3[0]}|{row3[1]}|{row3[2]}")

def assignvalue(mylist, index, letter):
    if mylist[index] == " ":
        mylist[index] = letter
    else:
        print("This cell is already filled")
        return False
    return True

def check(row1, row2, row3):
    if (row1[0] == row2[0] == row3[0] == "X") or (row1[1] == row2[1] == row3[1] == "X") or (row1[2] == row2[2] == row3[2] == "X") or (row1[0] == row1[1] == row1[2] == "X") or (row2[0] == row2[1] == row2[2] == "X") or (row3[0] == row3[1] == row3[2] == "X") or (row1[0] == row2[1] == row3[2] == "X") or (row1[2] == row2[1] == row3[0] == "X"):
        return "X"
    if (row1[0] == row2[0] == row3[0] == "O") or (row1[1] == row2[1] == row3[1] == "O") or (row1[2] == row2[2] == row3[2] == "O") or (row1[0] == row1[1] == row1[2] == "O") or (row2[0] == row2[1] == row2[2] == "O") or (row3[0] == row3[1] == row3[2] == "O") or (row1[0] == row2[1] == row3[2] == "O") or (row1[2] == row2[1] == row3[0] == "O"):
        return "O"
    return False

def tictactoe():
    player1 = input("Player1 enter your choice 'X' or 'O': ").upper()
    while player1 not in ['X', 'O']:
        player1 = input("Invalid choice! Player1, enter your choice 'X' or 'O': ").upper()
    player2 = "O" if player1 == "X" else "X"

    display(row1, row2, row3)
    for start in range(9):
        valid_move = False
        if start % 2 == 0:
            # Player 1's turn
            while not valid_move:
                i = int(input("Player1, enter which row (0, 1, 2): "))
                j = int(input("Enter which column (0, 1, 2): "))
                if 0 <= i <= 2 and 0 <= j <= 2:
                    valid_move = assignvalue([row1, row2, row3][i], j, player1)
                else:
                    print("Invalid input. Please enter a row and column between 0 and 2.")
        else:
            # Player 2's turn
            while not valid_move:
                i = int(input("Player2, enter which row (0, 1, 2): "))
                j = int(input("Enter which column (0, 1, 2): "))
                if 0 <= i <= 2 and 0 <= j <= 2:
                    valid_move = assignvalue([row1, row2, row3][i], j, player2)
                else:
                    print("Invalid input. Please enter a row and column between 0 and 2.")
        
        display(row1, row2, row3)
        winner = check(row1, row2, row3)
        if winner:
            print(f"{winner} is the winner!")
            break
    else:
        print("It's Draw")

if __name__ == "__main__":
    tictactoe()
