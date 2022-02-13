# CLI System
import sys


def helpprompt():
    print('_____ Camp Clerk CLI _____')
    print('| -h  Help Prompt |')
    print('| -v  Show Version |')
    print('__________________________')
    print('| -a  [Fullname] Camper Application Status |')
    print('| -an [Fullname] [Age] [Gender] [Address] Camper New Application |')
    print('| -aw [Fullname] Camper Withdraw Application |')
    print('__________________________')
    print('| -b  [Fullname] Camper Show Balance |')
    print('| -br [Fullname] [Amount] Camper Reduce Balance |')
    print('| -bc [Fullname] Camper Clear Balance |')
    print('__________________________')
    print('| -n  [Fullname] Camper Acceptance Status |')
    print('| -na [Fullname] Camper Accept |')
    print('| -nd [Fullname] Camper Decline |')
    print('__________________________')
    print('| -i  [Fullname] Camper Packet Status |')
    print('| -is [Fullname] [Date] Camper Packet Sent |')
    print('__________________________')


def statushandler(status, index, argv):
    argsarr = str(argv)
    print(argsarr)



def main(argv):
    status = 0
    index = 0
    argsarr = str(argv)
    for arg in argsarr:
        if arg == 'h':
            index+=1
            helpprompt()
            sys.exit(2)
        if arg == 'v':
            index+=1
            print('Build Feb132022')
            sys.exit(2)
        if arg == 'a':  # Grabs camper obj and prints app status
            index+=1
            statushandler(1,index,argsarr)
            sys.exit(2)
        if arg == 'an':  # Creates new camper obj
            index += 1
            statushandler(2, index, argsarr)
            sys.exit(2)
        if arg == 'aw':  # Removes camper obj
            index += 1
            statushandler(3, index, argsarr)
            sys.exit(2)
        if arg == 'b':  # Grabs camper obj and prints balance
            index += 1
            statushandler(4, index, argsarr)
            sys.exit(2)
        if arg == 'br':  # Modifies balance field in camper obj
            index += 1
            statushandler(5, index, argsarr)
            sys.exit(2)
        if arg == 'bc':  # Sets balance field to 0 in camper obj
            index += 1
            statushandler(6, index, argsarr)
            sys.exit(2)
        if arg == 'n':  # Grabs camper obj and prints acceptance status
            index += 1
            statushandler(7, index, argsarr)
            sys.exit(2)
        if arg == 'na':  # Modifies acceptance status field in camper obj to accepted
            index += 1
            statushandler(8, index, argsarr)
            sys.exit(2)
        if arg == 'nd':  # Modifies acceptance status field in camper obj to declined
            index += 1
            statushandler(9, index, argsarr)
            sys.exit(2)
        if arg == 'i':  # Grabs camper obj and prints packet status
            index += 1
            statushandler(10, index, argsarr)
            sys.exit(2)
        if arg == 'is':  # Modifies packet status field to sent & date
            index += 1
            statushandler(11, index, argsarr)
            sys.exit(2)
        else:
            index+=1


main(sys.argv[1:])
