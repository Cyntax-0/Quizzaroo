#Code for server and client Archetecture
import socket
import threading
import time

time.sleep(1)

header = 64  
format = 'utf-8'
port = 5050
ip = socket.gethostbyname(socket.gethostname())                                #used for automatically geting the ip address
#print(socket.gethostname())                                                   #used for getting the name of the host device info
ADDR = (ip,port)
# print(type(ip))
Deconnect_msg = "Connection lost."

Server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(ip)
Server.bind(ADDR)                                                              #used for binding ip address to this socket
print('The ip {} with port {}'.format(ip,port))



def handle_client(conn, addr):
    print(f"[New Connection]: {ADDR} connected. \n")

    connected = True
    while connected:
        msg_len = conn.recv(header).decode(format)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(format)
            if msg == Deconnect_msg:
                connected = False

            print(f'[{ADDR}] \n Name: {msg}')
            conn.send("Get Ready to Play: ".encode(format))
    
    conn.close()

def start():
    Server.listen()
    while True:
        conn, addr = Server.accept()                                            #used for blocking the processes until the next code
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        #Syntax of applying thread: thread = threading.Thread(target=class_name, args = (arguments))
        thread.start()

        print(f'[Activation]: {threading.active_count() - 1}')

print("[Starting]: Server side is starting... ")
start()
