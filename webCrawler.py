from request import Request
from parser import Parser

_DIR = "response"

def writeFile(fileName, fileType, content):

    mode = ('wb' if fileType == 'jpg' or fileType == "png" else 'w')

    f = open("{}/{}.{}".format(_DIR, fileName, fileType), mode)
    f.write(content)
    f.close()

class WebCrawler:

    def __init__(self, url, port=80):
        self.url = url
        self.port = port
        self.req = Request(url, port)


    def getImg(self, img):

        # Verificar se img é url absoluto ou relativo
        #
        #

        # Ex de imagem qualquer com url absoluto
        img = "purr.objects-us-east-1.dream.io/i/beerandcat.jpg" # Remover

        # Seleciona o nome e o tipo do arquivo
        img_name, img_type = img.split("/")[-1].split(".")

        req = Request(img, self.port)
        response = req.get()
        
        parser = Parser(response)
        data = parser.getImgData()

        # Salva o arquivo
        writeFile(img_name, img_type, data)


    def getContent(self):

        response = self.req.get()
        parser = Parser(response)
        html = parser.getHTML()

        # Salva o arquivo html
        writeFile("index", "html", html)

        imgs = parser.getImages()
        for img in imgs:
            self.getImg(img)
