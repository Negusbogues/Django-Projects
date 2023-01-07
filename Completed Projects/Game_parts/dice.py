import random
#dice roller
#display 2 int from 1-6
doubles = False
dice = [1,2,3,4,5,6]
roll = [random.choice(dice),random.choice(dice)]
if roll[0] == roll[1] and roll[0] != 1:
    doubles = True
    print(f"Doubles! \n{sum(roll)}, {roll}") 
if roll[0] == roll[1]:
    doubles = True
    if roll[0] == 1:
        print(f'Snake Eyes! \n{sum(roll)}, {roll}')
else:
    print(f"You rolled a {sum(roll)}, {roll}")