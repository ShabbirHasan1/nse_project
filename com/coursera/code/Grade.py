score = input("Enter score :")
try :
    score = float(score)
except:
    print("Invalid Input")
    quit()

if score > 1.0 :
    print("Invalid input")
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else :
    print('F')
