bottle = 99

while(bottle > 1):
    if bottle > 2:
        print("{} bottles of beers on the wall {} bottles of beer, take one down pass it around {} bottles of beer on the wall".format(bottle, bottle, bottle-1))
    else:
        print("{} bottles of beers on the wall {} bottles of beer, take one down pass it around {} bottle of beer on the wall".format(bottle, bottle, bottle-1))
    bottle = bottle-1
