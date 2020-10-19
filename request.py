import socket

_TIMEOUT = 2

class Request:

    def __init__(self, method, url, port):
        url = url.split("/", 1)
        self.metd = method
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
    def make_req(self, buff_size=1024):

        self.startSocket()
        
        request = "{} /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(self.metd, self.path, self.host)

        self.s.send(request.encode())

        response = self.s.recv(buff_size)
        response = response.decode()

        print(len(response))
        
        self.endSocket()

        return response

