import socket

HOST = "www.example.com" 
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

s.connect((HOST, PORT))
 
# request
request = "GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(HOST)

s.send(request.encode())  

response = s.recv(4096)

print(response.decode())

# response = ""
# while True:
#     recv = client.recv(1024)
#     if not recv:
#         break
#     response += str(recv)

s.close()
