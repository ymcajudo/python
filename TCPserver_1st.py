#https://realpython.com/python-sockets/#echo-server
#echo-server.py
#서버는 최초의 tcp client 연결이 끝나면 프로세스도 함께 종료

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")       #f string => https://www.daleseo.com/python-f-strings/
        while True:
            data = conn.recv(1024)          #TCP client에서 보낸 data를 byte()로 수신, 1024는 버퍼사이즈
            
            #Transform bytes to string, https://codechacha.com/ko/python-convert-bytes-to-string/
            response = "\nThe received message is " + "\""+ str(data,'utf-8') + "\"\n"      

            if not data:
                break
            conn.sendall(bytes(response,'utf-8'))       #Transform string to bytes, https://codechacha.com/ko/python-convert-string-to-bytes/




