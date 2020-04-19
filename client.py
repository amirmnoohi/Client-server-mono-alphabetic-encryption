import socket

import functions

HOST = '127.0.0.1'
PORT = 1104
try:
    s = socket.socket()
    s.connect((HOST, PORT))
    print(functions.bcolors.OKGREEN + "Connected To Server" + functions.bcolors.ENDC)
except ConnectionRefusedError:
    print(functions.bcolors.FAIL + "Can't Connect to Server\nMaybe Server is Down" + functions.bcolors.ENDC)
    exit(0)
try:
    while True:
        data = functions.enc_dec(str(input("Enter Data : ")).lower(), functions.gen(5), 1)
        while not data:
            print(functions.bcolors.WARNING + "Empty Message not Allowed" + functions.bcolors.ENDC)
            data = functions.enc_dec(str(input("Enter Data : ")).lower(), functions.gen(5), 1)
        s.send(data.encode("utf-8"))
        print(functions.bcolors.OKGREEN + "Sent : " + functions.bcolors.ENDC, data)
        data = functions.enc_dec(s.recv(65535).decode('utf-8'), functions.gen(5), 2)
        if not data:
            s.close()
            print(functions.bcolors.OKBLUE + "Connection Closed Successfully" + functions.bcolors.ENDC)
            exit(0)
        print("Server : ", data)
except KeyboardInterrupt:
    print(functions.bcolors.FAIL + "\nKeyboard Interrupt Pressed" + functions.bcolors.ENDC)
    s.close()
    print(functions.bcolors.FAIL + "Connection Closed" + functions.bcolors.ENDC)
