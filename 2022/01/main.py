import heapq


with open("C:/Users/Robert/Desktop/elf.txt", 'r') as f:
    elfs = f.read().splitlines()

tab = []
res = 0

for i in elfs:
    if i != '':
        res += int(i)
    else:
        tab.append(res)
        res = 0

print(max(tab))

# for i in elfs:
#     print(i)

result = heapq.nlargest(3, tab)

print(sum(result))