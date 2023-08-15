import socket
import os
import json

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',5002))

server.listen(5)
print("server listening on")
while True:
    print('waiting for connections')
    conn, addr = server.accept()
    print('Connected by', addr)
    while True:
        try:
            data = conn.recv(1024)
        except:
            break
        if not data:

            break
        # print('Received', repr(data))
        data = data.decode('utf-8')
        path = 'C:/Users/51276/Desktop/' + data
        print(path)
        filesize = os.path.getsize(path)
        headers = {'filesize':filesize}
        print(headers)
        header = json.dumps(headers).encode('utf-8')
        print(header)
        header_b =bytes(str(len(header)),'utf-8').zfill(4)
        conn.send(header_b)
        conn.send(header)
        print('*******')
        with open(path,mode='rb') as f:
            i =0
            while i < filesize:
                datas = f.read(1024)
                conn.send(datas)
                i += len(datas)
                print(i)
            f.close()
        print('*******')
    conn.close()
    print('Connection closed')

