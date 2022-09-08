from random import randint

wins = 0
iterator = 0
while iterator < 10:
    guess = int(input("Enter your guess (1 or 2): "))
    coin = randint(1, 2)
    iterator += 1
    if guess == coin:
        print(f'You are correct {guess} == {coin}.')
        wins += 1
    else:
        print(f'Sorry, {guess} != {coin}.')
print(f'You were correct {wins} times.')
