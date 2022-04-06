import socket
import sys
import time

if len(sys.argv) > 2:
    ip_addr = sys.argv[1]
    port = sys.argv[2]
else:
    ip_addr = input("Enter Switch's IP Address: ")
    port = input("Enter Port Number (Leave Blank for Default (6969)): ")

if port == "":
    port = '6969'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    while True:
        try:
            s.connect((ip_addr, int(port)))
            print("Socket Connection Success!")
            break
        except socket.error as msg:
            print("Couldn't connect to socket! Trying again in 5 seconds.")
            print(msg)
            time.sleep(5)


    while True:
        data = s.recv(1024)
        try:
            print(data.decode())
        except:
            print("Failed decoding data!")
        
        if not data:
            break
except KeyboardInterrupt:
    pass