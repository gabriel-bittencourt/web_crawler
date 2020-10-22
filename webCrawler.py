from urllib.parse import urlparse, urljoin

from request import Request
from parser import Parser

_DIR = "response"

def writeFile(fileName, fileType, content):

    mode = ('w' if fileType == 'html' else 'wb')

    f = open("{}/{}.{}".format(_DIR, fileName, fileType), mode)
    f.write(content)
    f.close()

class WebCrawler:

    def __init__(self, url, port=80):
        self.url = urlparse(url)
        self.port = port
        self.req = Request(self.url.netloc
                            + self.url.path, port)


    def handleImgSrc(self, imgSrc):
        url = urljoin(self.url.geturl(), imgSrc) # Trata caminhos absolutos e relativos
        parsedUrl = urlparse(url)
        httpPath = parsedUrl.netloc + parsedUrl.path

        return httpPath


    def getImg(self, img):

        
        img = self.handleImgSrc(img)

        # # Seleciona o nome e o tipo do arquivo
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
