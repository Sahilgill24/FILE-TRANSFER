import socket
import easygui as eg
import qrcode
import qrcode.image.pure

IP = "127.0.0.1"
PORT = 4999
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def send_file(file_path, conn):
    file_name = file_path.split("/")[-1]
    with open(file_path, "r") as f:
        text = f.read()
    
    # Send the choice to the server (UPLOAD)
    conn.send(f"UPLOAD@{file_name}@{text}".encode(FORMAT))
    
    response = conn.recv(SIZE).decode(FORMAT)
    cmd, msg = response.split("@")
    
    print(f"[SERVER]: {msg}")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"[SERVER]: {msg}")

        data = eg.enterbox("> ", "File Transfer", "Type your command:")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
        elif cmd == "UPLOAD":
            file_path = eg.fileopen
            file_path = eg.fileopenbox(title="Select a file to upload")
            if file_path:
                send_file(file_path, client)
                print(f"File '{file_path}' sent to the server.")
        elif cmd == "SCANQR":
            qr_code_path = eg.fileopenbox(title="Select a QR code image to scan")
            if qr_code_path:
                scan_qr_code(qr_code_path)
        elif cmd == "QUIT" or cmd is None:
            client.send("LOGOUT".encode(FORMAT))
            break

    print("Disconnected from the server.")
    client.close()

def scan_qr_code(qr_code_path):
    # Create a QR code scanner
    scanner = qrcode.Scanner()

    # Read the QR code from the specified image
    with open(qr_code_path, 'rb') as f:
        qr_code_data = scanner.scan(f.read())

    # Display the QR code data
    for code in qr_code_data:
        print(f"Scanned QR code data: {code.data}")

if __name__ == "__main__":
    main()
