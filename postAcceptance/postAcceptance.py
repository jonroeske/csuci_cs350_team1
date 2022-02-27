import datetime
from datatime import date
from objects.camper import Camper

# Clerk logic for camper post acceptance criteria
#cancellation refund
#90% within 3 weeks of acceptance and arrival instructions sent
#45% within 6 weeks of sending
#0% after this

def cancellationRefund(Camper):
    current_time = datetime.datetime.now()
    today = date(current_time.year, current_time.month, current_time.day)
    difference = (today - Camper.dateSentNotice).days / 7
    if 3 > difference:
        print("Cancelled within 3 weeks - 90% Refund")
        raiseBalance(Camper.fullName, 900)
        return False
    elif 6 > difference:
        print("Cancelled within 6 weeks - 45% Refund")
        raiseBalance(Camper.fullName, 450)
        return False
    else:
        print("Cancellation too late for refund")
        return False
