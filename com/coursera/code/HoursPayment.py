hrs = input("Enter Hours:")
h = float(hrs)
payment = input("Enter Hourly Payment:")
pay = float(payment)

totalPay = 0.0;
if h > 40 :
    h = h - 40
    totalPay = 40 * pay
    totalPay = totalPay + h * (pay * 1.5)
else :
    totalPay = h * pay
print (totalPay)