import random

def lotteryNumbers():
    listOfNumbers = []

    while len(listOfNumbers) < 5:
        a = random.randint(1,70)
        if a not in listOfNumbers:
            listOfNumbers.append(a)
    listOfNumbers.sort()

    m = random.randint(1,25)
    listOfNumbers.append(m)
    return listOfNumbers

print(lotteryNumbers())


# pool = list(range(1, 71))
# random.sample(pool, 5)

