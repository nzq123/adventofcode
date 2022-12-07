with open("elf6exc.txt", 'r') as f:
    elfs = f.read()

tab = []
result = 0

for i in elfs:
    result += 1
    if i not in tab:
        if len(set(tab)) == len(tab):
            print(result)
    if len(tab) != 4:
        tab.append(i)
    if len(tab) == 4:
        tab.pop(0)

