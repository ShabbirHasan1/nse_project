fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

handle = open(fname)
count = 0
for line in handle:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    count = count+1
    fromList = line.split()
    print(fromList[1])

print("There were", count, "lines in the file with From as the first word")