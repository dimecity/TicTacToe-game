the_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []
for key in the_board.keys():
    board_keys.append(key)

def print_board(board):
    print("""
{}|{}|{}
-+-+-
{}|{}|{}
-+-+-
{}|{}|{}
""".format(board['7'], board['8'], board['9'],
           board['4'], board['5'], board['6'],
           board['1'], board['2'], board['3']))

def main_game():    

    p_name1 = input("Enter player one's name: ")
    p_name2 = input("Enter player two's name: ")
    symbol = 'X'
    player = p_name1
    count = 0    

    for i in range(10):
        print_board(the_board)
        print("It's {}'s turn.".format(player))

        move = input()

        if move.isnumeric() == False or int(move) > 9:
            print("Invalid input. Must enter a number from 1-9. Enter again.\n")
            move = input()

        if the_board[move] == ' ':
            the_board[move] = symbol
            count += 1
        else:
            print("That space is already marked. Choose another spot")
            continue

        if count >= 5:
            if the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                print_board(the_board)
                print("GAME OVER!. {} WINS!".format(player))
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                print_board(the_board)
                print("GAME OVER!. {} WINS!".format(player))
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                print_board(the_board)
                print("GAME OVER!. {} WINS!".format(player))
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                print_board(the_board)
                print("GAME OVER!. {} WINS!".format(player))
                break
            elif the_board['3'] == the_board['5'] == the_board['7'] != ' ':
                print_board(the_board)
                print("GAME OVER!. {} WINS!".format(player))
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                print_board(the_board)
                print("GAME OVER!. {} WINS!".format(player))
                break
            elif the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                print_board(the_board)
                print("GAME OVER! {} WINS!".format(player))
                break
            elif count == 9:
                print("\nGame Over.")                
                print("TIE!!\n")
                break      

        if player == p_name1:
            player = p_name2
            symbol = 'O'
        else:
            player = p_name1
            symbol = 'X'

    restart = input("Retart game? (y/n)\n")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            the_board[key] = " "
        main_game()
    else:
        exit()
            
if __name__ == "__main__":            
    main_game()
            

       

       
            

            

        
        
    

       
        

    
