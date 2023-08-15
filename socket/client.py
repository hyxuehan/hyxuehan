import socket
import json
import os

class Myclient:
    def __init__(self, host:str ='127.0.0.1',port:int =5000,path:str =None,fiename:str = None):
        self.host = host
        self.port = port
        self.path = path.replace('\\', '/')
        self.fiename = fiename
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.client.connect((self.host, self.port))
        if fiename is None:
            files = os.walk(self.path)

    def file_transfer(self):
        self.client.send(self.fiename.encode('utf-8'))
        headers =self.client.recv(4).decode('utf-8')
        header_len = int(headers)
        header =self.client.recv(header_len)
        filesize =json.loads(header.decode('utf-8'))
        filesize = int(filesize.get('filesize'))
        path = self.path+self.fiename
        with open(path,mode='wb') as f:
            file_len =0
            while True:
                data = self.client.recv(4096)
                f.write(data)
                file_len += len(data)
                print(file_len)
                if file_len == filesize:
                    break
            f.close()
        print('*******')
    