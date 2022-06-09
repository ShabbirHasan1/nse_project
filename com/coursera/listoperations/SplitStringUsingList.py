handle = open('C:\\CourseraPython\\mbox-short.txt')
for line in handle:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    wordsList = line.split()
    if len(wordsList) > 2:
        #print(wordsList[2])
        domain = wordsList[1].split('@')
        print(domain[1])