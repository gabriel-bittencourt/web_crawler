from request import Request
from parser import Parser

_DIR = "response"

def writeFile(fileName, fileType, content):
    f = open("{}/{}.{}".format(_DIR, fileName, fileType), "w")
    f.write(content)
    f.close()

class WebCrawler:

    def __init__(self, url, port=80):
        self.url = url
        self.port = port
        self.req = Request('HEAD', url, port)

    def getContent(self):

        response = self.req.make_req()
        parser = Parser(response)
        length = int(parser.getHeader()['Content-Length'])

        self.req = Request('GET', self.url, self.port)
        response = self.req.make_req(length)
        parser = Parser(response)
        html = parser.getHTML()

        # Salva o arquivo html
        writeFile("index", "html", html)

        imgs = parser.getImages()
        for img in imgs:
            # Faz requisição
            # Salva o arquivo
            img = img
            pass

