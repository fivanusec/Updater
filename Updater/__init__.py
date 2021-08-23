import sys
from .runner import create_app


def run_updater(args):
    create_app(args=args)

def print_logo():
    print("\n")
    print("##     ## ########  ########     ###    ######## ######## ######## ")
    print("##     ## ##     ## ##     ##   ## ##      ##    ##       ##     ##")
    print("##     ## ##     ## ##     ##  ##   ##     ##    ##       ##     ##")
    print("##     ## ########  ##     ## ##     ##    ##    ######   ########")
    print("##     ## ##        ##     ## #########    ##    ##       ##   ##")
    print("##     ## ##        ##     ## ##     ##    ##    ##       ##    ##")
    print(" #######  ##        ########  ##     ##    ##    ######## ##     ##")
    print("\n")


def print_help():
    print("\
Usage: \n \
    --update, -U to update your repositories \n \
    --install, -I to install package \n \
    --remove, -R to remove package, \n \
    --autoremove, -AR to autoremove unused packages \n \
    ")


def main():
    if len(sys.argv) < 2:
        print_logo()
        print_help()
    else:
        print_logo()
        run_updater(sys.argv[1])


if __name__ == '__main__':
    main()
