import socket
import threading
import security
HEADER = 64
PORT = 9000
SERVER = socket.gethostbyname(socket.gethostname()) # my local ip -> fe80::7443:61d2:872f:f4ed%12 for server
FORMAT = 'utf-8'
print(SERVER)
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = '!disconnect'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    first = 0
    print(f'[NEW-CONNECTION] {addr} connected.')
    connectd = True
    while connectd:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connectd = False
            print(f'[{addr} : {msg}...]')
            conn.send("msg received".encode(FORMAT)) 
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'[ACTIVE-CONNECTIONS] {threading.activeCount()-1}')

print(F".......[STARTING-SERVER].......[LISTENING].....[{SERVER}]")
start()