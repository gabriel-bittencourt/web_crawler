import socket

_TIMEOUT = 2

class Request:

    def __init__(self, url, port):
        url = url.split("/", 1)
        self.host = url[0]
        self.path = "" if len(url)<=1 else url[1]
        self.port = port

    # Cria o socket
    def startSocket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.s.settimeout(_TIMEOUT)

    # Encerra o socket
    def endSocket(self):
        self.s.close()

    # Faz a requisição
    def get(self):

        self.startSocket()
        
        request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(self.path, self.host)

        self.s.send(request.encode())

        response = ""
        while True:
            try:
                recv = self.s.recv(2048)
            except socket.error as e:
                # print(e)
                break
            else:
                response += recv.decode()
        
        self.endSocket()

        return response

