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
        img_name = img.split("/")[-1]
        img_type = img_name.split(".")[-1]
        img_name = img_name[:-len(img_type)-1]

        req = Request(img, self.port)

        try:
            response = req.get()
        except:
            return
        
        response = req.get()
        data = Parser.getImgData(response)

        # Salva o arquivo
        writeFile(img_name, img_type, data)


    def getContent(self):

        try:
            response = self.req.get()
        except:
            return

        parser = Parser(response)
        html = parser.getHTML()

        # Salva o arquivo html
        writeFile("index", "html", html)

        imgs = parser.getImages()
        for img in imgs:
            self.getImg(img)
