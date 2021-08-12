import distro
import os
import sys


class AutoRemoveSwitch():
    def prepare(self, variant: str):
        return variant.replace(r" ", "_")

    def variant(self, variant: str):
        if(" " in variant):
            variant = self.prepare(variant)
        method = getattr(self, variant, lambda: "Invalid distro")
        return method()

    # Not Tested yet
    def Manjaro(self):
        os.system("sudo pacman -Rcns $(pacman -Qdtq)")

    # Not tested yet
    def Arch(self):
        os.system("sudo pacman -Rcns $(pacman -Qdtq)")

    def KDE_neon(self):
        os.system("sudo apt autoremove")

    def Ubuntu(self):
        os.system("sudo apt autoremove")


class InstallerSwitch():

    program = None

    def prepare(self, variant: str):
        return variant.replace(r" ", "_")

    def variant(self, variant: str, program: str):
        self.program = program
        if(" " in variant):
            variant = self.prepare(variant)
        method = getattr(self, variant, lambda: "Invalid distro")
        return method()

    # Not tested yet
    def Arch(self):
        os.system(f"sudo pacman -S {self.program}")

    # Not tested yet
    def Manjaro(self):
        os.system(f"sudo pacman -S {self.program}")

    def KDE_neon(self):
        os.system(f"sudo apt install {self.program}")

    def Ubuntu(self):
        os.system(f"sudo apt install {self.program}")


class RemoveSwitch():
    program = None

    def prepare(self, variant: str):
        return variant.replace(r" ", "_")

    def variant(self, variant: str, program: str):
        self.program = program
        if(" " in variant):
            variant = self.prepare(variant)
            method = getattr(self, variant, lambda: "Invalid distro")
            return method()

    # Not tested yet
    def Arch(self):
        os.system(f"sudo pacman -R {self.program}")

    # Not tested yet
    def Manjaro(self):
        os.system(f"sudo pacman -R {self.program}")

    def KDE_neon(self):
        os.system(f"sudo apt remove {self.program}")

    def Ubuntu(self):
        os.system(f"sudo apt remove {self.program}")


class Switch():
    def prepare(self, variant: str):
        return variant.replace(r" ", "_")

    def variant(self, variant: str):
        if(" " in variant):
            variant = self.prepare(variant)
        method = getattr(self, variant, lambda: "Invalid distro")
        return method()

    # Not tested yet
    def Arch(self):
        os.system("sudo pacman -Syu")

    # Not tested yet
    def Manjaro(self):
        os.system("sudo pacman -Syu")

    def KDE_neon(self):
        os.system("sudo apt update")
        os.system("sudo pkcon update")

    def Ubuntu(self):
        os.system("sudo apt update")
        os.system("sudo apt upgrade")


class AutoRemove():

    distro_variant = None

    def __init__(self):
        self.distro_variant = distro.linux_distribution()

    def run(self):
        print(
            f"Running autoremove on {self.distro_variant[0]}")
        run = AutoRemoveSwitch()
        run.variant(str(self.distro_variant[0]))


class Installer():

    distro_variant = None
    program = None

    def __init__(self):
        self.distro_variant = distro.linux_distribution()
        self.program = input("Input name of the program: ")

    def run(self):
        print(
            f"Running install for {self.program} on {self.distro_variant[0]}")
        run = InstallerSwitch()
        run.variant(str(self.distro_variant[0]), str(self.program))


class Update():

    distro_variant = None

    def __init__(self):
        self.distro_variant = distro.linux_distribution()

    def run(self):
        run = Switch()
        print(f"Running update for {self.distro_variant[0]}")
        run.variant(str(self.distro_variant[0]))


class Remove():

    distro_variant = None
    program = None

    def __init__(self):
        self.distro_variant = distro.linux_distribution()
        self.program = input("Input the name of the program: ")

    def run(self):
        print(f"Running remove for {self.program} on {self.distro_variant[0]}")
        run = RemoveSwitch()
        run.variant(str(self.distro_variant[0]), str(self.program))


class Method():
    def __init__(self, args: str):
        if("--update" in args or "-U" in args):
            method = Update()
            method.run()

        if("--install" in args or "-I" in args):
            method = Installer()
            method.run()

        if("--autoremove" in args or "-AR" in args):
            method = AutoRemove()
            method.run()

        if("--remove" in args or "-R" in args):
            method = Remove()
            method.run()


def print_logo():
    print(" \n \
╔╗─╔╗────╔╗──╔╗ \n \
║║─║║────║║─╔╝╚╗ \n \
║║─║╠══╦═╝╠═╩╗╔╬══╦═╗ \n \
║║─║║╔╗║╔╗║╔╗║║║║═╣╔╝ \n \
║╚═╝║╚╝║╚╝║╔╗║╚╣║═╣║ \n \
╚═══╣╔═╩══╩╝╚╩═╩══╩╝ \n \
────║║ \n \
────╚╝ \n \
")


def print_help():
    print_logo()
    print("\
Usage: \n \
    --update, -U to update your repositories \n \
    --install, -I to install package \n \
    --remove, -R to remove package, \n \
    --autoremove, -AR to autoremove unused packages \n \
    ")


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print_help()
    else:
        print_logo()
        run = Method(sys.argv[1])
