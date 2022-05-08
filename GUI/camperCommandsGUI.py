from GUI.guiHandler import *

def printCamperGUI(camper, **kwargs):
    if not isinstance(camper, Camper):
        return

    if "topBracket" in kwargs and kwargs["topBracket"] is True:
        print('|----------------------------------------------|')


    if "camperCreation" in kwargs and kwargs["camperCreation"] is True:
        print('  Name:    ' + camper.getName())
        print('  Age:     ' + str(camper.getAge()))
        print('  Gender:  ' + camper.getGender())
        print('  Address: ' + camper.getAddress())

    elif "attribute" in kwargs and isinstance(kwargs["attribute"], str):
        print('  Name:    ' + camper.getName())

        match kwargs["attribute"]:
            case "balance":
                print('  Balance:   $' + str(camper.getBalance()))
            case "applicationStatus":
                match camper.getAppStatus():
                    case 0:
                        print('  Application Status: Pending')
                    case 1:
                        print('  Application Status: Accepted')
                    case 2:
                        print('  Application Status: Rejected')
            case "packetStatus":
                pass # TODO - SIMPLIFY CAMPER VARIABLES
            case "session":
                match camper.getSession():
                    case 0:
                        print('  Session:     June')
                    case 1:
                        print('  Session:     July')
                    case 2:
                        print('  Session:     August')
                    case _:
                        print('  Session:     None')


    elif "simple" in kwargs and kwargs["simple"] is True:
        print('    Name:     ' + camper.getName())
        if camper.getAssignmentRequest():
            print('     Partner: ' + camper.getAssignment().getName())

    elif "detailed" in kwargs and kwargs["detailed"] is True:
        print('  Name:     ' + camper.getName())
        if camper.getAssignmentRequest():
            print('   Partner: ' + camper.getAssignment().getName())
        print('  Age:      ' + str(camper.getAge()))
        print('  Gender:   ' + camper.getGender())
        print('  Address:  ' + camper.getAddress())
        print('  Balance:  $' + str(camper.getBalance()))

        status = camper.getAppStatus()
        if status == 0:
            print('  Application Status: Pending')
        elif status == 1:
            print('  Application Status: Accepted')
            print('|----------------------------------------------|')

            session = camper.getSession()
            bunkhouse = camper.getBunkhouse()
            tribe = camper.getTribe()

            if session is not False:
                match session:
                    case 0:
                        print('  Session: June')
                    case 1:
                        print('  Session: July')
                    case 2:
                        print('  Session: August')

            if bunkhouse is not False:
                print('  Bunkhouse: ' + str(bunkhouse))
            if tribe is not False:
                print('  Tribe: ' + str(tribe))

            print('  Checked In: ' + str(camper.getCheckedIn()))
            print('  Packet Status: : ' + str(camper.getPacket()))

            packetDate = camper.getPacketSendDate()

            if packetDate:
                print('  Packet Sent Date: ' + str(packetDate))

        elif status == 2:
            print('  Application Status: Rejected')


    if "bottomBracket" in kwargs and kwargs["bottomBracket"] is True:
        print('|----------------------------------------------|')

