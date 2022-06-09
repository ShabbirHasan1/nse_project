name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

sentUserDict = dict()
for line in handle:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    userMailId = words[1]
    sentUserDict[userMailId] = sentUserDict.get(userMailId, 0) + 1

maxMailsSent = None
maxMailsSentCount = None

for key,val in sentUserDict.items() :
    if maxMailsSentCount == None or val > maxMailsSentCount:
        maxMailsSentCount = val
        maxMailsSent = key

print(maxMailsSent, maxMailsSentCount)