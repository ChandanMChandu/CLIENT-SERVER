import socket

s = socket.socket()

ip="localhost"
port=5545

s.connect((ip,port))

print("hi connected")

#s.send(b"1234")
s.send(b"this is client information")
info = s.recv(1024)
print(info)

info1 = raw_input()

s.send(bytes(info1))

