import re
print(sum([int(i) for i in re.findall('[0-9]+', open('C:\\CourseraPython\\regex_sum_605440.txt').read())]))