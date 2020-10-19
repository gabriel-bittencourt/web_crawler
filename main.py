import socket
from bs4 import BeautifulSoup # parser

HOST = "www.columbia.edu" 
DIR = "/~fdc"
FILE = "sample.html"
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

s.connect((HOST, PORT))
 
# request
request = "GET {}/{} HTTP/1.1\r\nHost:{}\r\n\r\n".format(DIR, FILE, HOST)

s.send(request.encode())  
s.settimeout(2)

# response = s.recv(4096)

# print(response.decode())

response = ""
while True:
    try:
        recv = s.recv(1024)
    except socket.error as e:
        print(e)
        break
    else:
        response += recv.decode()

soup = BeautifulSoup(response, 'html.parser')
print(soup)

for imgTag in soup.find_all('img'):
    imgSrc = imgTag.get('src')
    # faz requisição
    print(imgSrc)

s.close()
