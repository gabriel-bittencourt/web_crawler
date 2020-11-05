from bs4 import BeautifulSoup


class Parser(BeautifulSoup):

    def __init__(self, content):
        self.__rawContent = content
        self.__header = None

    # Retorna uma string com apenas o conteúdo HTML
    def getHTML(self):
        p = self.__rawContent.find(b'\r\n\r\n')
        if p >= 0:
            html = self.__rawContent[p+8:]
        else: 
            html = self.__rawContent
        super().__init__(html, 'html5lib')
        return str(self.html.prettify())

    # Retorna um vetor com as imagens
    def getImages(self):

        imgs = []
        for imgTag in self.find_all('img'):
            imgSrc = imgTag.get('src')
            imgs.append(imgSrc)

        return imgs

    # Retorna a header em forma de dicionário
    def getHeader(self):
        if self.__header == None:
            self._createHeader()
        return self.__header

    def _createHeader(self):
        header_dict = {}
        header_str = self.__rawContent.split(b'\r\n\r\n')[0]
        header_lines = header_str.split(b'\r\n')

        # Código de status
        header_dict['Status'] = int(header_lines[0].split()[1])

        # Outras infos
        for line in header_lines[1:]:
            if line:
                key, val = line.split(b': ')
                key = key.decode()
                key = val.decode()

                header_dict[key] = val

        self.__header = header_dict

    # def getImgData(self):
    #     return self.__rawContent.split(b'\r\n\r\n')[-1]

    @staticmethod
    def getImgData(data):
        return data.split(b'\r\n\r\n')[-1]
