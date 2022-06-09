handle = open('C:\\CourseraPython\\mbox-short.txt')

for line in handle:
    if line.startswith('From:'):
        print(line.strip('\n'))


