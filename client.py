import os
import socket
import easygui as eg
import qrcode


IP = socket.gethostbyname(socket.gethostname())

PORT = 4999
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def qr(file_path):
    qr_1=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_L,box_size=10,border=4)
    server_url = "http://192.168.67.188:5000/server/" # you have to put your computers ip here 
    file_name=os.path.basename(file_path)
    print(file_name)
    
    qr_1.add_data(f'{server_url}{file_name}')
    print(f'{server_url}{file_name}')
    qr_1.make(fit=True)
    qr_img=qr_1.make_image()
    
    print("showing qr code")
    qr_img.show()

def send_file(file_path,client):
    file_name=os.path.basename(file_path)
    print(file_name)
    with open(file_path,"rb") as f:
        client.send(file_name.encode(FORMAT))
        data=f.read(SIZE)
        file_data=client.send(data)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    msg=client.recv(SIZE).decode(FORMAT)
    x=input(f"{msg} if yes then type (y) otherwise (n)")
    if x == "y":
        file_path=eg.fileopenbox(title="Select a file to send : ")
        send_file(file_path,client)
        qr(file_path)
        
    else:
        print(f"client does not want to send file ")


if __name__=="__main__":
    main()




