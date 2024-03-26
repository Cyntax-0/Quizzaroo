import socket

header = 64
port = 5050
format = 'utf - 8'
disconnect_message = "Connection lost"

server_code = input('Enter the code: ')                           #for geeting to connected to the server.
server_code = str(server_code)
server = server_code

Addr = (server,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(Addr)
print('Connection Stablished... ')

def send(msg):
    message = msg.encode(format)
    msg_len = len(message)
    send_len = str(msg_len).encode(format)
    send_len += b' ' *  (header - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(format))

send(input('Enter your Game Name: '))
input()

send(disconnect_message)
