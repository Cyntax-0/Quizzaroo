import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
print("Server side")

# for ip address:
ip = socket.gethostbyname(socket.gethostname()) #this line gets the ip address of the computer automatically
# ip = '127.0.0.1'
port = 5050
serverSocket.bind((ip, port))

print("server ip {} port {}".format(ip, port))

serverSocket.listen()

count = 0

while(True):
    (clientConnection, clientAddress) = serverSocket.accept()
    count += 1
    #print("Accepted {} connections".format(count))
    print(f"Accepted {count} connections")

    while(True):
        data = clientConnection.recv(1024)
        print(data)

        if (data != ""):
            msg1 = "Good Moring... "
            msg2 = "hello Guys... "

            msg1Bytes = str.encode(msg1)
            msg2Bytes = str.encode(msg2)

            clientConnection.send(msg1Bytes)
            clientConnection.send(msg2Bytes)

            print("Connection stablished")
            break

