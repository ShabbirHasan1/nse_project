fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words :
        if not lst.__contains__(word):
            lst.append(word)

lst.sort()
for word in lst:
    print(word)