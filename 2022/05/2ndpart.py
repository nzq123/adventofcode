with open("elf5exc.txt", 'r') as f:
    elfs = f.read().splitlines()

tab = [
    ["INDEX0"],
    list("NBDTVGZJ"),
    list("SRMDWPF"),
    list("VCRSZ"),
    list("RTJZPHG"),
    list("TCJNDZQF"),
    list("NVPWGSFM"),
    list("GCVBPQ"),
    list("ZBPN"),
    list("WPJ")
]

new_tab = []

for lines in elfs:
    if len(lines) != 0:
        split_lines = lines.split()
        if split_lines[0] == 'move':
            for rows in range(int(split_lines[1])):
                new_tab.append(tab[int(split_lines[3])].pop())
            for rows in range(int(split_lines[1])):
                tab[int(split_lines[5])].append(new_tab.pop())
for lines in tab:
    print(lines[-1])

