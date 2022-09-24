"""
File Name: Tic-Tac-Toe

Author: Zack Doxey

Purpose: Two Player Tic-Tac-Toe Game
"""

the_board = {'1': '1' , '2': '2' , '3': '3' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '7': '7' , '8': '8' , '9': '9' }

board_keys = []

for key in the_board:
    board_keys.append(key)

# Print Board
def print_board(board):
    print(f"{board['1']} | {board['2']} | {board['3']}")
    print("- + - + -")
    print(f"{board['4']} | {board['5']} | {board['6']}")
    print("- + - + -")
    print(f"{board['7']} | {board['8']} | {board['9']}")


# Function which has all the gameplay functionality
def main():

    turn = 'X'
    count = 0


    for i in range(10):
        print_board(the_board)
        move = input(f"{turn}'s turn to choose a square (1-9): ")    
        print()  

        if the_board[move] == "1" or the_board[move] == "2" or the_board[move] == "3" or the_board[move] == "4" or the_board[move] == "5" or the_board[move] == "6" or the_board[move] == "7" or the_board[move] == "8" or the_board[move] == "9":
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            
            # win across the top
            if the_board['1'] == the_board['2'] == the_board['3'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")
                print()                
                print(f"Good Job! {turn} WON!")                
                break
            
            # win across the middle
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")                
                print()
                print(f"Good Job! {turn} WON!")
                break
            
            # win across the bottom
            elif the_board['7'] == the_board['8'] == the_board['9'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")                
                print()
                print(f"Good Job! {turn} WON!")
                break
            
            # win down the left side
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")                
                print()                
                print(f"Good Job! {turn} WON!")
                break
            
            # win down the middle
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")                
                print()                
                print(f"Good Job! {turn} WON!")
                break
            
            # win down the right side
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")                
                print()                
                print(f"Good Job! {turn} WON!")
                break 
            
            # win diagonal
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")                
                print()                
                print(f"Good Job! {turn} WON!")
                break
            
            # win diagonal
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ': 
                print_board(the_board)
                print()
                print("Game Over.")                
                print()                
                print(f"Good Job! {turn} WON!")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print()
            print("Game Over.")                
            print()                 
            print("It's a Tie!")
            break

        # Change the player's turn after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # # Ask if player wants to restart the game
    # restart = input("Do want to play Again?(y/n)")
    # if restart.lower() == "y":  
    #     for key in board_keys:
    #         the_board[key] = " "

    #     main()

if __name__ == "__main__":
    main()
