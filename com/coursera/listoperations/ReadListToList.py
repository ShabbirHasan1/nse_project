inputList = list()
while True :
    value = input('Enter value:')
    if value == 'done':
        break
    try :
        inputList.append(float(value))
    except :
        print("Invalid Value")

print(sum(inputList), sum(inputList)/len(inputList))
