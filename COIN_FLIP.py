import random

def coin(n):
    result = []
    for i in range(n): 
        i = random.randint(0,1)
        result.append(i)
    
    return result


def countR(n):
    zeros = 0
    ones = 0
    for i in n:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1

    return(f'Heads {ones}, Tails: {zeros}')

coins = coin(100)

#  Call function in terminal
#  countR(coins)
