handle = open('C:\\CourseraPython\\abc.txt')
wordCount = 0;
for line in handle :
    words = line.split()
    wordCount = wordCount + words.__len__()

print(wordCount)