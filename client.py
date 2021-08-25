import socket

HEADER = 64
PORT = 5050
SERVER = 'YOUR_IP_ADDRESS'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

print('Double press the enter to exit')
print('Enter the message')
msg = 'msg'
while msg != '':
    msg = input('> ')
    if len(msg):
        send(msg)
    else:
        send(DISCONNECT_MESSAGE)

print('Exited')