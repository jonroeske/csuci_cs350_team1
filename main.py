# CLI System
import sys


def main(argv):
    opts, args = str(argv)
    for opt, arg in opts:
        if opt == '-h':
            print('Help')
            sys.exit(2)
        elif opt in ():
            print('')
            sys.exit(2)


main(sys.argv[1:])
