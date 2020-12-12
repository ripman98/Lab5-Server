import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Berjaya buat sockett")

local="192.168.114.6"
port=20001

s.bind((local,port))

print("Berjaya bind socket di port:"+str(port))


print("Socket tengah menunggu client!")

while True:
	c,addr=s.accept()
	print("Dapat capaian dari: "+str(addr))

	c.send(b'Terima Kasih!')

	buffer=c.recv(1024)
	print(buffer)

c.close()
