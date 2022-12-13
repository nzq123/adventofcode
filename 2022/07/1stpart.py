with open("elf7exc.txt", 'r') as f:
    elfs = f.read().splitlines()[2:]


class Catalog:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.catalogs = []
        self.files = []

    def get_file_size(self):
        result = 0
        for i in self.files:
            result += i.size
        return result

    def get_catalog_size(self):
        result = 0
        for i in self.catalogs:
            result += i.get_size()
        return result

    def get_size(self):
        if len(self.catalogs) == 0:
            return self.get_file_size()
        else:
            return self.get_file_size() + self.get_catalog_size()

    def get_catalog_by_name(self, catalog_name):
        for i in self.catalogs:
            if i.name == catalog_name:
                return i
        return None


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size


root_catalog = current_catalog = Catalog(name='/', parent=None)

for elf in elfs:
    elf_after_split = elf.split(' ')
    if elf_after_split[0] == 'dir':
        current_catalog.catalogs.append(Catalog(name=elf_after_split[1], parent=current_catalog))
    if elf_after_split[1] == 'cd':
        if elf_after_split[2] == '..':
            current_catalog = current_catalog.parent
        else:
            current_catalog = current_catalog.get_catalog_by_name(elf_after_split[2])
    if elf_after_split[0].isdigit():
        current_catalog.files.append(File(name=elf_after_split[1], size=int(elf_after_split[0])))

print(root_catalog.get_size())

global result
result = 0


def count_size(node):
    global result
    if node is None:
        return
    for child in node.catalogs:
        if child.get_size() <= 100000:
            result += child.get_size()
        count_size(child)


count_size(root_catalog)
print(result)


# current_catalog.catalogs.append(Catalog(name='fwbjchs', parent=current_catalog))
# current_catalog.catalogs.append(Catalog(name='hmnpr', parent=current_catalog))
#
# current_catalog = current_catalog.get_catalog_by_name('fwbjchs')
#
# current_catalog.files.append(File(name='wqdlv.mdw', size=15))
# current_catalog.files.append(File(name='wvbnz', size=21))
# current_catalog.catalogs.append(Catalog(name='testfold', parent=current_catalog))
#
# current_catalog = current_catalog.get_catalog_by_name('testfold')
# current_catalog.files.append(File(name='testfile', size=10))
#
# print(current_catalog.get_size(), current_catalog.name)
#
# print(root_catalog.get_size(), root_catalog.name)

# current_catalog = current_catalog.parent
#
# print(current_catalog.get_size(), current_catalog.name)
#
# current_catalog = current_catalog.parent
#
# print(current_catalog.get_size(), current_catalog.name)
#
# current_catalog = current_catalog.get_catalog_by_name('hmnpr')
#
# print(current_catalog.name)






