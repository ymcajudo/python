#https://realpython.com/python-sockets/#echo-server
# echo-server.py
#최초 연결이 종료 되어도 프로세스는 진행 중

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

while True:

    socServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socServer.bind((HOST, PORT))
    socServer.listen()
    conn, addr = socServer.accept()
    print(f"Connected by {addr}")
    
    while True:
            data = conn.recv(1024)          #TCP client에서 보낸 data를 byte()로 수신, 1024는 버퍼사이즈
            
            #Transform bytes to string, https://codechacha.com/ko/python-convert-bytes-to-string/
            response = "\nThe received message is " + "\""+ str(data,'utf-8') + "\"\n"      

            if not data:
                break
            """
            if str(data,'utf-8') == "kill the process":     #Client에서 서버 프로세스 중지 시킬 때
                break
            """
            conn.sendall(bytes(response,'utf-8'))       #Transform string to bytes, https://codechacha.com/ko/python-convert-string-to-bytes/
    
    conn.close()

    """
    if str(data,'utf-8') == "kill the process":
        break
    """
  