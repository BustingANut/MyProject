from ftplib import FTP as ftp
import time
global domain, user, passwd

class Downloader:
    def __init__(self):
        self.data = bytes()
    def __call__(self, data):
        self.data += data

def logindata():
    domain = raw_input(" \nDomain of the FTP Server: ")
    user = raw_input(" \nYour username: ")
    passwd = raw_input(" \nYour password: ")
    try:
        ftp.connect(domain)
    except:
        print " \n[!] Unable to connect to Server !"
        time.sleep(1)
        logindata()
    try:
        ftp.login(user, passwd)
        print " \nYou are now logged in! "
    except:
        print " \n[!] Wrong username or password! "
        time.sleep(1)
        logindata()

def menu():
    print """ \nOptions:
                        [1] Change directory
                        [2] Delete file
                        [3] Make new directory
                        [4] Show directory content
                        [5] Show path of the current directory
                        [6] Rename file
                        [7] Remove directory
                        [8] Show file size
                        [9] Upload files to the FTP Server
                        [10] Download files from the FTP Server
                        [11] Exit """
    eingabe = raw_input(" \n< ")
    if eingabe == "1":
        pathname = raw_input(" \nPathname ")
        try:
            ftp.cwd(pathname)
        except:
            print " \n[!]Incorrect pathname! "
            menu()
    elif eingabe == "2":
        filename = raw_input(" \nFile to delete: ")
        try:
            ftp.delete(filename)
        except:
            print " \n[!]File not found! "
            time.sleep(1)
            menu()
    elif eingabe == "3":
        drname = raw_input(" \nName of the new directoty: ")
        ftp.mkd(drname)
    elif eingabe == "4":
        pathname = raw_input(" \nPath of the directory: ")
        try:
            for x in ftp.mlsd():
                print " \n{}: {} ".format(x[0], x[1]["type"])
        except:
            print " \n[!]Unable to show content! "
            time.sleep(1)
            menu()
    elif eingabe == "5":
        ftp.pwd()
    elif eingabe == "6":
        filenamefrom = raw_input(" \nFile to change name: ")
        filenameto = raw_input(" \nNew name: ")
        try:
            ftp.rename(filenamefrom, filenameto)
        except:
            print " \n[!]Unable to change filename! "
            time.sleep(1)
            menu()
    elif eingabe == "7":
        dirname = raw_input(" \nName of the directory to delete: ")
        try:
            ftp.rmd(dirname)
        except:
            print " \n[!]Unable to delete directory! "
            time.sleep(1)
            menu()
    elif eingabe == "8":
        filename = raw_input(" \nFilename: ")
        try:
            ftp.size(filename)
        except:
            print " \n[!]Unable to show filesize! "
            time.sleep(1)
            menu()
    elif eingabe == "9":
        download = Downloader()
        filename = raw_input(" \nFile to download: ")
        filename = "RETR " + filename
        try:
            ftp.retrbinary(filename, download)
        except:
            print " \n[!]Unable to download file! "
            time.sleep(1)
            menu()
    elif eingabe == "10":
        filename = raw_input(" \nFile to upload: ")
        try:
            open(filename, "rb")
        except:
            print " \nFile not found! "
            time.sleep(1)
            menu()
        filename = "STOR " + filename
        try:
            ftp.storbinary(filename, f)
            print " \nFile uploaded! "
            upload.close()
        except:
            print " \n[!]Unable to upload file! "
            time.sleep(1)
            menu()
    elif eingabe == "11":
        print " \nGoodbye! "
        time.sleep(2)
        exit()

logindata()
while True:
    menu()
