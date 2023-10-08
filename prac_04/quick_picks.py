import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_OF_QUICK_PICKS_PER_LINE = 6
NUMBER_OF_QUICK_PICKS = int(input("How many quick picks? "))
for i in range(NUMBER_OF_QUICK_PICKS):
    quick_pick = []
    while len(quick_pick) < NUMBERS_OF_QUICK_PICKS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    quick_pick = [str(number) for number in quick_pick]
    print(" ".join(quick_pick))
