a = [1, 2, 3]
b = [4, 5, 6]
c = b+a
c.append(7)

c.sort()
for cValue in c :
    print(cValue)

print(max(c))
print(min(c))
print(sum(c))
print(len(c))
print(sum(c)/len(c))
