from random import randint
# A simple game, guess 1 or 2
user_guess = int(input("What is your guess (1 or 2): "))
coin = randint(1, 2)
if user_guess == coin:
    print(f'You win! {user_guess} == {coin}')
else:
    print(f'You lose! {user_guess} != {coin}')
