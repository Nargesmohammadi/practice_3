import math

math.sin(math.pi / 2)


def printTwice(bruce):
    print(bruce, bruce)


printTwice('Ali')
printTwice(math.sin(math.pi / 2))

statel = "Don't worry!"
print(statel)

printTwice(printTwice('samp' * 4))
printTwice(statel)


def catTwice(part1, part2):
    cat = part1 + part2
    printTwice(cat)


first = "Try Again, Don't Be Despair"
second = "I Believe That You Can Do This"
catTwice(first, second)
