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
        if "http" not in url[:5]:
            url = "http://" + url
        self.url = urlparse(url)
        self.port = port
        self.req = Request(self.url.hostname
                            + self.url.path, port)


    def handleImgSrc(self, imgSrc):
        url = urljoin(self.url.geturl(), imgSrc) # Trata caminhos absolutos e relativos
        parsedUrl = urlparse(url)
        httpPath = parsedUrl.hostname + parsedUrl.path

        return httpPath


    def getImg(self, img):

        
        img = self.handleImgSrc(img)

        # # Seleciona o nome e o tipo do arquivo
        img_file = img.split("/")[-1]
        img_type = img_file.split(".")[-1]
        img_name = img_file[:-len(img_type)-1]

        req = Request(img, self.port)

        try:
            response = req.get()
        except:
            return
        
        response = req.get()
        data = Parser.getImgData(response)
        
        parser = Parser(response)
        header = parser.getHeader()
        if header['Status'] == 200:
            # Salva o arquivo
            writeFile(img_name, img_type, data)
        else:
            print(f'Requisição de "{img}" retornou status {header["Status"]}. Ignorando imagem...')


    def getContent(self):

        try:
            response = self.req.get()
        except:
            return

        parser = Parser(response)
        header = parser.getHeader()

        if header["Status"] == 200:

            # Salva o arquivo html
            html = parser.getHTML()
            writeFile("index", "html", html)

            imgs = parser.getImages()
            for img in imgs:
                self.getImg(img)
        else:
            print(f'Requisição HTML retornou status {header["Status"]}. Terminando...')
