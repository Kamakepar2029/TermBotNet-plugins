import socket
sock = socket.socket()

sock.connect(('localhost', 8080))
data = sock.send('Hello Man'.encode())

sock.close

print(data)