import random

name = input("Please input your name: ")
print(f'Hello {name}, Welcome to the game')

rpc = ['ROCK', 'SCISSOR', 'PAPER']

bot_win_count = 0
user_win_count = 0
want_to_play = "Y"

while True:
    bot_input = random.randint(0, 2)
    user_input = input("Please type Rock, Paper or Scissor: ").upper()
    if bot_win_count == 2:
        print("You lost. try again")
        want_to_play = input("Press Y to play again or N to end: ").upper()
        if want_to_play == 'Y':
            user_win_count = 0
            bot_win_count = 0
        else:
            break

    if user_win_count == 2:
        print("You won")
        want_to_play = input("Press Y to play again or N to end: ").upper()
        if want_to_play == 'Y':
            user_win_count = 0
            bot_win_count = 0
        else:
            break

    if rpc[bot_input] == user_input:
        print("its a draw")
        print(rpc[bot_input])
        pass

    elif (user_input == "ROCK" and rpc[bot_input] == 'PAPER') or (
            user_input == "PAPER" and rpc[bot_input] == 'SCISSOR') or (
            user_input == "SCISSOR" and rpc[bot_input] == 'ROCK'):
        bot_win_count += 1
        print(f"You lost {bot_win_count} times")

    # elif user_input== "" 'PAPER' and rpc[bot_input] == "ROCK" or (rpc[bot_input]== "PAPER" and  user_input== 'SCISSOR') or (rpc[bot_input]== "SCISSOR" and  user_input== 'ROCK'):
    else:
        user_win_count += 1
        print(f"You won {user_win_count} times")
