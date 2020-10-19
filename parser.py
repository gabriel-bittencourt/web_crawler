from bs4 import BeautifulSoup


class Parser(BeautifulSoup):

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
            # faz requisição
            # print(imgSrc)

        return imgs
