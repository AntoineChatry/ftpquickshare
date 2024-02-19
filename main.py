from ftplib import FTP, error_perm
import time
import sys
import os

ftp = FTP()
ftp.connect("yourftpip", 21)
ftp.login("login", "password")
ftp.cwd("yourdir")

print(f"Starting upload for: {sys.argv[1]}")

def upload(ftp, path):
    if os.path.isfile(path):
        print(f"Uploading file: {path}")
        with open(path, "rb") as file:
            ftp.storbinary("STOR " + os.path.basename(path), file)
    elif os.path.isdir(path):
        print(f"Creating directory: {os.path.basename(path)}")
        try:
            ftp.mkd(os.path.basename(path))
        except error_perm as e:
            if not e.args[0].startswith("550"):
                raise
        ftp.cwd(os.path.basename(path))
        for name in os.listdir(path):
            upload(ftp, os.path.join(path, name))
        ftp.cwd("..")



upload(ftp, sys.argv[1])

ftp.quit()
