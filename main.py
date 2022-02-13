# CLI System
import sys
import camper


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


def main(argv):
    args = str(argv)
    for arg in args:
        if arg == 'h':
            helpprompt()
            sys.exit(2)
        if arg == 'v':
            print('Alpha 0.1; Build Feb132022')
            sys.exit(2)
        if arg == 'a': # Grabs camper obj and prints app status
            print('')
            sys.exit(2)
        if arg == 'an': # Creates new camper obj
            print('')
            sys.exit(2)
        if arg == 'aw': # Removes camper obj
            print('')
            sys.exit(2)
        if arg == 'b': # Grabs camper obj and prints balance
            print('')
            sys.exit(2)
        if arg == 'br': # Modifies balance field in camper obj
            print('')
            sys.exit(2)
        if arg == 'bc': # Sets balance field to 0 in camper obj
            print('')
            sys.exit(2)
        if arg == 'n': # Grabs camper obj and prints acceptance status
            print('')
            sys.exit(2)
        if arg == 'na': # Modifies acceptance status field in camper obj to accepted
            print('')
            sys.exit(2)
        if arg == 'nd': # Modifies acceptance status field in camper obj to declined
            print('')
            sys.exit(2)
        if arg == 'i': # Grabs camper obj and prints packet status
            print('')
            sys.exit(2)
        if arg == 'is': # Modifies packet status field to sent & date
            print('')
            sys.exit(2)


main(sys.argv[1:])
