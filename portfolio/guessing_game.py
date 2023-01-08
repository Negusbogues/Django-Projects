import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 10
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if count == 0 :
            print('The human has failed')
            break
        elif guess < random_number:
            print("Sorry, guess again. Too low.")
            count -= 1
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
            count -= 1
    if count == 0:
        print('Skynet has launched!')
    else:
        print("Congratulations, you win!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 10
    print(f'Pick a number between {low} & {high}')
    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if count == 0:
            print('The android has failed!')
            break
        elif feedback == 'h':
            high = guess - 1
            count -= 1
        elif feedback == 'l':
            low = guess + 1
            count -= 1
        elif feedback == 'c':
            break
        else:
            print('Invalid Entry')
    if count == 0:
        print('We will rebuild.')
    else:
        print('Congradulations, the android found your number!')

try:
    x = 999
    range = (random.randint(1, x))
    range2 = (random.randint(1, x,))
    range3 = (random.randint(1, x))
    lotto = [range, range2, range3]
    print(lotto)
    guess(range)
    computer_guess(range)

except ValueError:
    print('Please be honest.' + "\n" + "We're done here....")