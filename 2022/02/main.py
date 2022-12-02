with open("elf2exc.txt", 'r') as f:
    elfs = f.read().splitlines()

computer = 0
player = 0

# KOMPUTER
# A = ROCK
# B = PAPER
# C = SCIZOR
#
# Y = PAPER 2
# X = ROCK 1
# Z = SCIZOR 3
#
# WIN = 6, DRAW = 3, LOSE = 0
#
# Y = DRAW
# X = LOSE
# Z = WIN


for i in elfs:
    if i[0] == 'A' and i[2] == 'Y':
        player += 4
    if i[0] == 'A' and i[2] == 'X':
        player += 3
    if i[0] == 'A' and i[2] == 'Z':
        player += 8
    if i[0] == 'B' and i[2] == 'Y':
        player += 5
    if i[0] == 'B' and i[2] == 'X':
        player += 1
    if i[0] == 'B' and i[2] == 'Z':
        player += 9
    if i[0] == 'C' and i[2] == 'Y':
        player += 6
    if i[0] == 'C' and i[2] == 'X':
        player += 2
    if i[0] == 'C' and i[2] == 'Z':
        player += 7

print(player)




