from itertools import product
from pyfiglet import figlet_format
import string
print(figlet_format("El tekito\nWord list Generator", font="cybermedium"))
minIndex = int(input("el_tekito@Wordlister [min] -> "))
maxIndex = int(input("el_tekito@Wordlister [max] -> "))
letters = input("el_tekito@Wordlister [letters or random (N)] -> ")
txtFile = input("el_tekito@Wordlister [Text File Location] -> ")
print("[+] creating word list please wait..")
counter = 0
charecter = ""


if letters == "n":
    charecter = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
else:
    charecter = letters


fileOpen = open(txtFile, "w")
for i in range(minIndex, maxIndex+1):
    for j in product(charecter,repeat=i):
        word = "".join(j)
        fileOpen.write(word)
        fileOpen.write("\n")
        counter += 1

print("[+] word list created, there are {0} word".format(counter))
wordlst = input("el_tekito@Wordlister [do you want to see the word list (y - n) ] -> ")
if wordlst == "y":
    fileOpen.close()
    fileOpen = open(txtFile, "r")
    print("[+] {0}\n{1}".format(txtFile, fileOpen.read()))
    fileOpen.close()
else :
    print("bye bye")