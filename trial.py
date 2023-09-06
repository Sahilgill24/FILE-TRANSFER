import easygui as eg
import os
import qrcode

file_path=eg.fileopenbox(title="file")
print(os.path.basename(file_path))

qr_1=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_L,box_size=10,border=4)
server_url = "http://192.168.236.168:5000/file/"
file_url=f"file://{file_path}"
qr_1.add_data(server_url + file_url)
qr_1.make(fit=True)
qr_img=qr_1.make_image()
qr_img.show()