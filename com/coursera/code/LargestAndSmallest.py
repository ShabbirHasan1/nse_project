largest = None
smallest = None
while True:
    intVal = input('Enter Value :')
    if intVal == 'done':
        break
    try :
        intVal = int(intVal)
    except:
        print('Invalid input')
        continue
    if largest is None :
        largest = intVal
    elif largest < intVal:
        largest = intVal
    if smallest is None :
        smallest = intVal
    elif smallest > intVal:
        smallest = intVal
print('Maximum is', largest)
print('Minimum is', smallest)