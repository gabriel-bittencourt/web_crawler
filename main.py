import socket

HOST = "www.columbia.edu" 
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

s.connect((HOST, PORT))
 
# request
request = "GET /~fdc/sample.html HTTP/1.1\r\nHost:{}\r\n\r\n".format(HOST)

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

print(response)

s.close()
