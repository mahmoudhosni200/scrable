

# Welcome Message
welcome_messages = '''** Welcome to Number Scrabble Game ** 
The way of playing : 
1. This Game is played by two players with a list of numbers between 1 and 9 
2. Each player takes turns picking a number from the list 
3. Notice that: Once a number has been picked, it can't be picked again. 
4. If a player has picked three numbers that add up to 15, that player wins the game.
5. However, if all the numbers are used and no player gets exactly 15, the game is a draw.
'''
print(welcome_messages)


def display_board():
    print("Player 1 Numbers:", N_Player1)
    print("Player 2 Numbers:", N_Player2, "\n")

#Function For Check Winner
def check_winner(player_numbers):
    if len(player_numbers) >= 3:
        for i in range(len(player_numbers) - 2):
            for j in range(i + 1, len(player_numbers) - 1):
                for k in range(j + 1, len(player_numbers)):
                    if player_numbers[i] + player_numbers[j] + player_numbers[k] == 15:
                        return True
    return False

# While Loop
while True:
    # The List Of Numbers
    N_Scrabble = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    N_Player1 = []
    N_Player2 = []
    print("\nPlease Enter What Do You Want To Do:\n1) Play\n2) Exit")
    start = input('Enter Your Choice[1 -- 2] : ')
    if start == '1':
        while True:
            while True:
                try:
                    move = int(input(f"Player 1, pick a number: {N_Scrabble}\n"))
                    if move in N_Scrabble:
                        N_Scrabble.remove(move)
                        N_Player1.append(move)
                        break
                    else:
                        print("Invalid move. Please pick a number from the available list.\n")
                except ValueError:
                    print("Invalid input. Please enter a number.\n")
        #Check Player 1 Win
            if check_winner(N_Player1):
                display_board()
                N_Player1.clear()
                N_Player2.clear()
                print("Player 1 wins!")
                break

            if not N_Scrabble:
                display_board()
                print("It's a draw!")
                N_Player1.clear()
                N_Player2.clear()
                break
            display_board()

            # Player 2's turn
            while True:
                try:
                    move = int(input(f"Player 2, pick a number From: {N_Scrabble}\n"))
                    if move in N_Scrabble:
                        N_Scrabble.remove(move)
                        N_Player2.append(move)
                        break
                    else:
                        print("Invalid move. Please pick a number from the available list.\n")
                except ValueError:
                    print("Invalid input. Please enter a number.\n")
        #Check Player 2 Win
            if check_winner(N_Player2):
                display_board()
                N_Player2.clear()
                N_Player1.clear()
                print("Player 2 wins!")
                break

            if not N_Scrabble:
                display_board()
                print("It's a draw!")
                N_Player1.clear()
                N_Player2.clear()
                break
            display_board()

    elif start == '2':
        print("Exit The Game...")
        exit()
    else:
        print("Please enter a valid choice")