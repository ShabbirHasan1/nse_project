import datetime
import time


def isClosingTime():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    if hour >= 15 and minute >= 30:
        return True
    return False

def sleep10mins() :
    time.sleep(1 * 60)  # wait ten minutes

def sleep3mins() :
    time.sleep(3 * 60)  # wait 3 minutes