fname = input("Enter file name: ")
fh = open(fname)
totalFloatVal = 0
lineCount = 0;
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    index = line.find('X-DSPAM-Confidence:')
    index = index + len('X-DSPAM-Confidence:')
    totalFloatVal = totalFloatVal + float(line[index:])
    lineCount = lineCount + 1

print('Average spam confidence:',totalFloatVal/lineCount)
