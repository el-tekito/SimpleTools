from getpass import getpass
import pyAesCrypt
import os

def IslemOne(dir):
    passwd = getpass("el_tekito@Blocked [Password] ->")
    buffersize = 512*1024
    pyAesCrypt.encryptFile(str(dir),str(dir)+".eltekito",passwd,buffersize)
    print("[+] Succesfull -> {0}.eltekito".format(str(dir)))


dir = input("el_tekito@Blocked [File Location] ->")
IslemOne(dir)
os.remove(dir)