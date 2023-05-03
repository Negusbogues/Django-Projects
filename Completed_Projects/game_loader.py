game_list = ['Tictactoe', 'Snake', 'Shooter', 'Guessing']
print("Welcome to the game console.\nWhich game would you like to play?")
print(game_list)
while True:
    pick = input("Game: ").capitalize()
    if pick in game_list:
        if pick == 'Tictactoe':
            from Game_parts import tictactoe
            continue
        elif pick == 'Snake':
            from Game_parts import snake_game
            continue
        elif pick == 'Shooter':
            from Game_parts import shooter
            continue
        elif pick == 'Guessing':
            from Game_parts import guessing_game
            continue
    elif pick == 'Quit' or pick == 'Q':
        print('Console shutting down.')
        break
    else:
        print("Please make a valid selection.\nOr you can enter 'quit' to end.")
        continue