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

    def Manjaro():
        os.system("sudo pacman -Rcns $(pacman -Qdtq)")
    # Not tested yet

    def Arch():
        os.system("sudo pacman -Rcns $(pacman -Qdtq)")

    def KDE_Neon():
        os.system("sudo apt autoremove")

    def Ubuntu():
        os.system("sudo apt autoremove")


class AutoRemove():

    distro_variant = None

    def __init__(self):
        self.distro_variant = distro.linux_distribution()

    def run(self):
        print(
            f"Running autoremove on {self.distro_variant[0]}")
        run = AutoRemoveSwitch()
        run.variant(str(self.distro_variant[0]))


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


class Method():
    def __init__(self, args: str):
        if("-U" in args):
            method = Update()
            method.run()

        if("-I" in args):
            method = Installer()
            method.run()

        if("-AR" in args):
            method = AutoRemove()
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
    -U to update your repositoris \n \
    -I <package_name> to install package \n \
    -AR to autoremove unused packages \n \
    ")


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print_help()
    else:
        print_logo()
        run = Method(sys.argv[1])
