hours = float(input("Enter hours worked: "))
payPerHour = float(input("Enter Amount to be paid fpr hour: "))


def calculatePayment(h, pay):
    if h > 40:
        h = h - 40
        totalpay = 40 * pay
        totalpay = totalpay + h * (pay * 1.5)
    else:
        totalpay = h * pay
    return totalpay


print(calculatePayment(hours, payPerHour))
