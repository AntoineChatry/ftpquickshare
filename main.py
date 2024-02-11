from ftplib import FTP
import time
import sys
import os

file_path = sys.argv[1]
ftp = FTP()
ftp.connect("yourftpip", 21)

# Login to the FTP server
ftp.login("login", "password")
# switch directory to
ftp.cwd("yourdir")
with open(file_path, "rb") as f:
    ftp.storbinary("STOR " + os.path.basename(file_path), f)
# sleep for 1 seconds
time.sleep(1)

# Logout from the FTP server
ftp.quit()
