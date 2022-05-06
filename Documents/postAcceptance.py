import datetime
from Documents.docHandler import raiseBalance

# Clerk logic for camper post acceptance criteria
# Cancellation refund
# 90% within 3 weeks of acceptance and arrival instructions sent
# 45% within 6 weeks of sending
# 0% after this


def cancellationRefund(camper):
    current_time = datetime.datetime.now()
    today = datetime.date(current_time.year, current_time.month, current_time.day)
    difference = (today - camper.dateSentNotice).days / 7
    if 3 > difference:
        print("Cancelled within 3 weeks - 90% Refund")
        raiseBalance(camper.fullName, -900)
        return False
    elif 6 > difference:
        print("Cancelled within 6 weeks - 45% Refund")
        raiseBalance(camper.fullName, -450)
        return False
    else:
        print("Cancellation too late for refund")
        return False


def withdrawCamper(camper, campers, tribes, bunkhouses):
    cancellationRefund(camper)
    campers.remove(camper)
    for tribe in tribes:
        if tribe.contains(camper):
            tribe.remove(camper)
    for bunkhouse in bunkhouses:
        if bunkhouse.contains(camper):
            bunkhouse.remove(camper)
