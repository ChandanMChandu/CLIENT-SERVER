import socket
import numpy as np
s=socket.socket()

ip=""
port=np.random.randint(5000,6000,1)

s.bind((ip,port))
dynamic = s.getsockname()
print(port)
print(dynamic)
s.listen(5)

while(1):
	conn,addr =  s.accept()
	msg = conn.recv(1024)
	#sum=0
	#if msg.isdigit():

		#for i in msg:
			#sum=sum+int(i)

		#conn.send(bytes(sum))
	#else:
		#conn.send(b"sorry this cannot be done")

	print(msg)

	conn.send(b"send the msg to save in a file")

	msg2=conn.recv(1024)
	with open("anupam.txt","w") as f:
		f.write(msg2)

		f.close()

