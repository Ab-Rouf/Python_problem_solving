#find duplicate data in a list
l1=["ai", "ml", "python", "ml", "dl", "ai"]
unique=set()
duplicate=set()

for element in l1:
    if element not in unique:
        unique.add(element)
    elif element not in duplicate:
        duplicate.add(element)
dup=list(duplicate)
print(dup)
