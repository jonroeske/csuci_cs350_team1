from Handlers.dataHandler import summerCamp

from Handlers.guiHandler import *

def viewBalance():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        mainMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return

    clearScreen()
    printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)
    showPrompt("Press 'Enter' to Return!", bottomBracket=True)
    mainMenu()


def processPayment():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        mainMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return
    elif camper.getBalance() <= 0:
            mainMenu()
            showMessage("Balance is fully paid!", bottomBracket=True)
            return

    while True:
        clearScreen()

        printCamperGUI(camper, attribute="balance", topBracket=True, bottomBracket=True)

        try:
            amount = float(showPrompt("What size payment would you like to make?", prompt="($0 is minimum balance!)", bottomBracket=True))
        except ValueError:
            showMessage("Invalid input!", bottomBracket=True, wait=2)
            continue

        clearScreen()
        showMessage("Old balance:", topBracket=True, bottomBracket=True)
        printCamperGUI(camper, attribute="balance")

        amount = camper.getBalance() - amount

        if amount < 0:
            camper.setBalance(0)
        else:
            camper.setBalance(amount)
        break


    showMessage("New balance:",topBracket=True, bottomBracket=True)
    printCamperGUI(camper, attribute="balance")

    showPrompt("Press 'Enter' to Return!", topBracket=True, bottomBracket=True)
    mainMenu()


def processRefund():
    clearScreen()
    name = showPrompt("Please insert camper name:", prompt="(First + Last)", topBracket=True, bottomBracket=True)

    camper = summerCamp.searchCamper(name)

    if camper == STATUS_CODES["NO_CAMPER"]:
        camperSubMenu()
        showMessage("That camper doesn't exists!", bottomBracket=True)
        return
    elif camper.getBalance() >= 1000:
        mainMenu()
        showMessage("No payments were made!", bottomBracket=True)
        return


    while True:
        clearScreen()

        balance = camper.getBalance()
        refund = 1000 - balance

        if camper.getAppNoticeIsSent() is False and balance < 1000:
            showMessage(["Due to not having been sent an acceptance notice, you are eligible for a FULL refund!",
                        "Refund: $" + str(refund)], topBracket=True, bottomBracket=True)

        elif camper.getAppNoticeIsSent() is True and balance < 1000:
            weekDifference = abs((camper.getDateAppNoticeSent() - Objects.values.TODAYS_DATE).days/7)

            if abs((camper.getDateAppNoticeSent() - Objects.values.TODAYS_DATE).days) < 1:
                showMessage(["Due to requesting a refund on the same day as Sign-Up,",
                                 " You are eligible for a FULL refund!",
                                 "Paid:   $" + str(1000 - balance),
                                 "Refund: $" + str(refund)], topBracket=True, bottomBracket=True)

            elif weekDifference < 3:
                refund = (1000-balance) - ((1000-balance) * 0.1)
                showMessage(["Due to requesting a refund less than three weeks after acceptance notice,",
                             " You will be receiving 90% of original payment. ",
                             "Paid:   $" + str(1000 - balance),
                             "Refund: $" + str(refund)], topBracket=True, bottomBracket=True)

            elif weekDifference < 6:
                refund = (1000-balance) - ((1000-balance) * 0.55)
                showMessage(["Due to requesting a refund less than six weeks after acceptance notice,",
                             " You will be receiving 45% of original payment. ",
                             "Paid:   $" + str(1000 - balance),
                             "Refund: $" + str(refund)], topBracket=True,bottomBracket=True)

            elif weekDifference >= 6:
                while True:
                    clearScreen()
                    showMessage(["Due to requesting a refund after six weeks since the acceptance notice,",
                                 " You are not eligible for a refund at this time."], topBracket=True)

                    confirmation = showPrompt("Would you like to reset your balance anyways?", prompt='"Y" for Yes, "N" for No', bottomBracket=True)

                    if confirmation == 'Y':
                        camper.setBalance(1000.00)
                        mainMenu()
                        return
                    elif confirmation == 'N':
                        mainMenu()
                        return
                    else:
                        showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)


        confirmation = showPrompt("Would you like to continue with refund?", prompt='"Y" for Yes, "N" for No', bottomBracket=True)
        if confirmation == 'Y':
            break
        elif confirmation == 'N':
            mainMenu()
            return
        else:
            showMessage('Must be "Y" or "N"', bottomBracket=True, wait=2)

    clearScreen()
    showMessage(["Refund granted!", " Refund amount: $" + str(refund)], topBracket=True, bottomBracket=True)

    camper.setBalance(1000.00)
    summerCamp.updateCamper(camper)

    showPrompt("Press 'Enter' to Return!", bottomBracket=True)
    mainMenu()