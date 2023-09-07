import os 
import socket
import threading 

IP = socket.gethostbyname(socket.gethostname())
PORT = 4999
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server/"


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("DO YOU WANT TO SEND THE FILE ".encode(FORMAT))
    filename=conn.recv(SIZE).decode(FORMAT)
    if not os.path.exists(SERVER_DATA_PATH):
        name=os.mkdir(SERVER_DATA_PATH)
        file=os.path.join(name,filename)
        print("is this running ")
        with open(file,"wb") as f:
            data=conn.recv(SIZE)
            f.write(data)
            print("file recieved")
    else:
        file=os.path.join(SERVER_DATA_PATH,filename)
        with open(file,"wb") as f:
            data=conn.recv(SIZE)
            f.write(data)
            print("file recieved")

def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()
