with open("elf4exc.txt", 'r') as f:
    elfs = f.read().splitlines()

result = 0

for i in elfs:
    elfs_range = i.split(",")
    first_range = elfs_range[0].split("-")
    second_range = elfs_range[1].split("-")
    if int(first_range[0]) <= int(second_range[0]) <= int(first_range[1]):
        result += 1
    elif int(second_range[0]) <= int(first_range[0]) <= int(second_range[1]):
        result += 1
print(result)

