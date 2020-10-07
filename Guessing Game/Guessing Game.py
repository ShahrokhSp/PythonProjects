from random import randint
while True:
    Goal = randint(1,100)
    PA1 = int(input('Take your Guess pls: '))
    if PA1<1 or PA1>100:
        print('OUT OF BOUND')
        continue
    elif abs(PA1-Goal)>10:
        print('COLD')
    elif abs(PA1-Goal)<10:
        print('WARM')
    count = 1
    while Goal != PA1:
        PA2 = int(input('Again: '))
        if abs(PA1-Goal)>abs(PA2-Goal):
            print('Warmer')
        elif abs(PA1-Goal)<abs(PA2-Goal):
            print('Colder')
        PA1 = PA2
        count += 1
    print('Egjacly')
