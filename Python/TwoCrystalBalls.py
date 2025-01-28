import math

def twoCrystalBalls(floors):
    step = round(math.sqrt(len(floors)))
    brokenAt = 0

    for i in range(0, len(floors), step):
        if floors[i]:
            brokenAt = i - step
            break
    
    if brokenAt == 0:
        brokenAt = len(floors) - step

    for i in range(brokenAt, brokenAt + step + 1):
        if floors[i]:
            brokenAt = i
            break
    return brokenAt


print(twoCrystalBalls([False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True]))