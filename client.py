import socket

socketObject = socket.socket()

socketObject.connect(("localhost", 5050))
print("Connected to localhost")

msg = "Hi Server"
Bytes = str.encode(msg)

socketObject.sendall(Bytes)

while(True):
    data = socketObject.recv(1024)
    print(data)

    if not data:
        print("Connection closed")
        break
socketObject.close()