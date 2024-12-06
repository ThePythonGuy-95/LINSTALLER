import os
import time
import webbrowser

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    print("LINSTALLER VER. 1.0")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Choose an available distro:")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("- 1. Ubuntu")
    print("- 2. Debian")
    print("- 3. Linux Mint")
    print("- 4. Arch Linux")
    print("- 5. OpenSUSE")
    print("- 6. Fedora")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("This will install the LATEST version. For distros that have long-term and short-term support releases (Like Ubuntu),")
    print("this utility will install the long term releases.")
    print("--------------------------------------------------------------------------------------------------------------------------")
    distro = input("Option: ")
    
    if distro == "1":
        print("Loading...")
        time.sleep(3)
        clear_screen()
        print("Connecting to the server...")
        time.sleep(3)
        clear_screen()
        ubuntu()
    elif distro == "2":
        print("Loading...")
        time.sleep(3)
        clear_screen()
        print("Connecting to the server...")
        time.sleep(3)
        clear_screen()
        debian()
    elif distro == "3":
        print("Loading...")
        time.sleep(3)
        clear_screen()
        print("Connecting to the server...")
        time.sleep(3)
        clear_screen()
        mint()
    elif distro == "4":
        print("Loading...")
        time.sleep(3)
        clear_screen()
        print("Connecting to the server...")
        time.sleep(3)
        clear_screen()       
        arch()
    elif distro == "5":
        print("Loading...")
        time.sleep(3)
        clear_screen()
        print("Connecting to the server...")
        time.sleep(3)
        clear_screen()
        openSuse()
    elif distro == "6":
        print("Loading...")
        time.sleep(3)
        clear_screen()
        print("Connecting to the server...")
        time.sleep(3)
        clear_screen()
        fedora()
    else:
        print("Option not valid. Try again with a valid option.")
        time.sleep(3)
        clear_screen()
        main()

def ubuntu():
    webbrowser.open("https://releases.ubuntu.com/24.04.1/ubuntu-24.04.1-desktop-amd64.iso")
    print("Opening your browser...")
    time.sleep(7)
    clear_screen()
    print("Done! Returning to main menu...")
    time.sleep(7)
    clear_screen()
    main()


def debian():
    webbrowser.open("https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.8.0-amd64-netinst.iso")
    print("Opening your browser...")
    time.sleep(7)
    clear_screen()
    print("Done! Returning to main menu...")
    time.sleep(7)
    clear_screen()
    main()

def mint():
    webbrowser.open("https://mirrors.layeronline.com/linuxmint/stable/22/linuxmint-22-cinnamon-64bit.iso")
    print("Opening your browser...")
    time.sleep(7)
    clear_screen()
    print("Done! Returning to main menu...")
    time.sleep(7)
    clear_screen()
    main()

def arch():
    webbrowser.open("https://geo.mirror.pkgbuild.com/iso/2024.12.01/archlinux-2024.12.01-x86_64.iso")
    print("Opening your browser...")
    time.sleep(7)
    clear_screen()
    print("Done! Returning to main menu...")
    time.sleep(7)
    clear_screen()
    main()

def openSuse():
    webbrowser.open("https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Build710.3-Media.iso")
    print("Opening your browser...")
    time.sleep(7)
    clear_screen()
    print("Done! Returning to main menu...")
    time.sleep(7)
    clear_screen()
    main()

def fedora():
    webbrowser.open("https://download.fedoraproject.org/pub/fedora/linux/releases/41/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-41-1.4.iso")
    print("Opening your browser...")
    time.sleep(7)
    clear_screen()
    print("Done! Returning to main menu...")
    time.sleep(7)
    clear_screen()
    main()

main()
