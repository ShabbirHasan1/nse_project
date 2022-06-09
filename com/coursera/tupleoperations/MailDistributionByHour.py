name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = dict()
for line in handle :
    if not line.startswith('From') or line.startswith('From:'):
        continue
    lineSplit = line.split()
    timeSplit = lineSplit[5].split(':')
    time[timeSplit[0]] = time.get(timeSplit[0],0) + 1

sortedList = sorted(time.items())
for k,v in sortedList:
    print(k, v)
