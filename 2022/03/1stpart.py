with open("elf3exc.txt", 'r') as f:
    elfs = f.read().splitlines()

result = 0

for i in elfs:
    firstpart, secondpart = i[:len(i) // 2], i[len(i) // 2:]
    for firstletter in firstpart:
        if firstletter in secondpart:
            if firstletter == firstletter.upper():
                result += ord(firstletter) - 38
                break
            else:
                result += ord(firstletter) - 96
                break

print(result)

