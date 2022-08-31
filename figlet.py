from pyfiglet import figlet_format

def figletpyt(a):
    print(figlet_format(a, font="acrobatic"))
    print(figlet_format(a, font="3-d"))
    print(figlet_format(a, font="3x5"))
    print(figlet_format(a, font="cybermedium"))#
    print(figlet_format(a, font="univers"))
    print(figlet_format(a, font="big"))#
    print(figlet_format(a, font="isometric3"))

figletText = input("> ")
figletpyt(figletText)