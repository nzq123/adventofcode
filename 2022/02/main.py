with open("elf2exc.txt", 'r') as f:
    elfs = f.read().splitlines()

computer = 0
player = 0

for i in elfs:
    if i[0] == 'A' and i[2] == 'Y':
        player += 8
    if i[0] == 'A' and i[2] == 'X':
        player += 4
    if i[0] == 'A' and i[2] == 'Z':
        player += 3
    if i[0] == 'B' and i[2] == 'Y':
        player += 5
    if i[0] == 'B' and i[2] == 'X':
        player += 1
    if i[0] == 'B' and i[2] == 'Z':
        player += 9
    if i[0] == 'C' and i[2] == 'Y':
        player += 2
    if i[0] == 'C' and i[2] == 'X':
        player += 7
    if i[0] == 'C' and i[2] == 'Z':
        player += 6

print(player)

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



