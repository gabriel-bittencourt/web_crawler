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

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print("Erro ao criar socket: {}\n".format(err))
            raise
        else:
            try:
                s.connect((self.host, self.port))
            except socket.gaierror as err:
                print("Erro ao se conectar a \"{}\"".format(self.host))
                raise
            else:
                s.settimeout(_TIMEOUT)
                return s

    # Encerra o socket
    def endSocket(self):
        self.s.close()

    # Faz a requisição
    def get(self):

        try:
            self.s = self.startSocket()
        except:
            raise
        
        request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(self.path, self.host)

        self.s.send(request.encode())

        response = self.s.recv(2048)
        while True:
            try:
                recv = self.s.recv(2048)
            except socket.timeout as e:
                break
            else:
                response += recv
        
        self.endSocket()

        return response
