import random




def numbers_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('guess a number:'))

        if user_guess == answer:
            print(f"correct! firse khelo loude {user_guess}")
            break


        if user_guess < answer:
            print(f'{user_guess} is too low!')

        else:
            print(f'{user_guess} is too high!')

numbers_game()
