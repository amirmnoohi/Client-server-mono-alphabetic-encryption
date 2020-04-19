import socket

import functions

HOST = '127.0.0.1'
PORT = 1104
try:
    s = socket.socket()
    s.bind((HOST, PORT))
    print(functions.bcolors.OKGREEN + "Server Started Successfully" + functions.bcolors.ENDC)
except socket.error:
    print(
        functions.bcolors.FAIL + "Enabling the server has encountered a problem\nTry Another Time" + functions.bcolors.ENDC)
s.listen()
conn, addr = s.accept()
try:
    while True:
        data = functions.enc_dec(conn.recv(65535).decode('utf-8'), functions.gen(5), 2)
        print("Client : ", data)
        if not data:
            print(functions.bcolors.WARNING + "Disconnect Tcp Packet Recieved" + functions.bcolors.ENDC)
            data = 'good bye'
        if data == 'good bye':
            conn.close()
            print(functions.bcolors.OKBLUE + "Connection Closed Successfully" + functions.bcolors.ENDC)
            exit(0)
        data = functions.enc_dec(str(input("Enter Data : ")).lower(), functions.gen(5), 1)
        conn.send(data.encode("utf-8"))
        print(functions.bcolors.OKGREEN + "Sent : " + functions.bcolors.ENDC, data)
except KeyboardInterrupt:
    print(functions.bcolors.FAIL + "Keyboard Interrupt Pressed" + functions.bcolors.ENDC)
    s.close()
    print(functions.bcolors.FAIL + "Connection Closed" + functions.bcolors.ENDC)

