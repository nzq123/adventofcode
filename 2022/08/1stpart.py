with open("elf8exc.txt", 'r') as f:
    elfs = f.read().splitlines()

result = 0

tab = []

for i in elfs:
    tab2 = []
    for j in i:
        tab2.append(int(j))
    tab.append(tab2)

print(tab)


for i in range(len(tab)):
    for j in range(len(tab[i])):
        k = i
        m = i
        p = j
        q = j
        cond1 = True
        cond2 = True
        cond3 = True
        cond4 = True
        while k > 0:
            k -= 1
            if tab[k][j] < tab[i][j]:
                pass
            else:
                cond1 = False
        while m < len(tab[i]) - 1:
            m += 1
            if tab[m][j] < tab[i][j]:
                pass
            else:
                cond2 = False
        while p > 0:
            p -= 1
            if tab[i][p] < tab[i][j]:
                pass
            else:
                cond3 = False
        while q < len(tab[j]) - 1:
            q += 1
            if tab[i][q] < tab[i][j]:
                pass
            else:
                cond4 = False
        print(tab[i][j], cond1, cond2, cond3, cond4)
        if cond1 or cond2 or cond3 or cond4:
            result += 1

print(f'result: {result}')
