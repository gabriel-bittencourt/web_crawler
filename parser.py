from bs4 import BeautifulSoup


class Parser(BeautifulSoup):

    __header__ = None

    def __init__(self, content):
        super().__init__(content, 'html.parser')

    # Retorna uma string com apenas o conteúdo HTML
    def getHTML(self):
        return str(self.html)

    # Retorna um vetor com as imagens
    def getImages(self):

        imgs = []
        for imgTag in self.find_all('img'):
            imgSrc = imgTag.get('src')
            imgs.append(imgSrc)

        return imgs

    # Retorna a header em forma de dicionário
    def getHeader(self):
        if self.__header__ == None:

            header_dict = {}
            header_str = str(self).split('<!DOCTYPE HTML>')[0]
            lines = header_str.split('\r\n')

            # Código de status
            header_dict['Status'] = int(lines[0].split()[1])

            # Outras infos
            for line in lines[1:]:
                if line:
                    key, val = line.split(': ')
                    header_dict[key] = val

            self.__header__ = header_dict

        return self.__header__
