import socket
import security
HEADER = 64
PORT = 9000
SERVER = '192.168.175.232'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) 


def authentication():
    global user
    user = input("username : ")
    if user in security.allowed_users:
        password = input("password : ")
        if password == security.allowed_users[user]:
            print("AUTHENTICATION CONFIRMED")
        else:
            print("WRONG PASSOWORD")
            authentication()
    else:
        print('UNAUTHORISED USER')
        authentication()        
authentication()


def send(msg):
    message = msg.encode(FORMAT)
    msg_length  = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))
msg = ''
first = 0
while msg!=DISCONNECT_MESSAGE:
    msg = input()
    send(msg+" by "+user)
send(DISCONNECT_MESSAGE)