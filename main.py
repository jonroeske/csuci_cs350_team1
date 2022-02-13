# CLI System
import sys


def helpprompt():
    print('----- Camp Clerk CLI -----')
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
    print('| -is [Fullname] Camper Packet Sent |')
    print('__________________________')


def main(argv):
    opts, args = str(argv)
    for opt, arg in opts:
        if opt == '-h':
            helpprompt()
            sys.exit(2)
        elif opt == '-b':
            print('Alpha 0.1; Build Feb122022')
            sys.exit(2)


main(sys.argv[1:])
