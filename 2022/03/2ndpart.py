with open("elf3exc.txt", 'r') as f:
    elfs = f.read().splitlines()

result = 0

for i in range(0, len(elfs), 3):
    firstword = elfs[i]
    secondword = elfs[i + 1]
    thirdword = elfs[i + 2]
    for firstletter in firstword:
        if firstletter in secondword and firstletter in thirdword:
            if firstletter == firstletter.upper():
                result += ord(firstletter) - 38
                break
            else:
                result += ord(firstletter) - 96
                break
print(result)

