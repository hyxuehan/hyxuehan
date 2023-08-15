import socketserver
import os
import json

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        print(self.client_address)
        while True:
            
            try:
                data = self.request.recv(1024)
            except:
                break
            if not data:

                break
            # print('Received', repr(data))
            data = data.decode('utf-8')
            path = 'C:/Users/51276/Desktop/' + data
            print(path)
            filesize = os.path.getsize(path)
            headers = {'filesize': filesize}
            print(headers)
            header = json.dumps(headers).encode('utf-8')
            print(header)
            header_b = bytes(str(len(header)), 'utf-8').zfill(4)
            self.request.send(header_b)
            self.request.send(header)
            print('*******')
            with open(path, mode='rb') as f:
                i = 0
                while i < filesize:
                    datas = f.read(1024)
                    self.request.send(datas)
                    i += len(datas)
                    print(i)
                f.close()
            print('*******')
        self.request.close()
        print('Connection closed')

       
        # pass

sk = socketserver.ThreadingTCPServer(('127.0.0.1',5000),MyTCPHandler)
print('server started')
sk.serve_forever()
