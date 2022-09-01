from getpass import getpass
import pyAesCrypt
import os

def IslemTwo(dir):
    passwd = getpass("el_tekito@Blocked [Password] ->")
    buffersize = 512*1024
    pyAesCrypt.decryptFile(str(dir),str(dir)+".txt",passwd,buffersize)
    print("[+] Succesfull -> {0}.txt".format(str(dir)))

dir = input("el_tekito@DeBlocked [File Location] ->")

IslemTwo(dir)
os.remove(dir)
