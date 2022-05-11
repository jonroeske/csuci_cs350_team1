from Objects.values import STATUS_CODES, changeDate, resetDate
from Handlers.uiHandler import debugSubMenu, clearScreen, showMessage, showPrompt

def changeTodaysDate():
    while True:
        clearScreen()
        date = showPrompt("What would you like to set today's date to?",
                          prompt=["(Month)/(Day)/(Year)", "Example: 12/25/1998", "Press 'Enter' to Return!"], topBracket=True, bottomBracket=True)

        result = changeDate(date)

        if result == STATUS_CODES["ARGUMENT_ERROR"]:
            showMessage("Invalid input!", bottomBracket=True, wait=2)
        elif result == STATUS_CODES["SUCCESS"]:
            break

    clearScreen()
    debugSubMenu()
    showMessage("Date change successful!", bottomBracket=True)


def resetTodaysDate():
    resetDate()

    debugSubMenu()
    showMessage("Date reset successful!", bottomBracket=True)