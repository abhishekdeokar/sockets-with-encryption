import socket
import hashlib
from Crypto.Cipher import AES

KEY = hashlib.sha256("some random password").digest()

IV = "abcdefghijklmnop"
obj = AES.new(KEY, AES.MODE_CFB, IV)

def main():
	host = "127.0.0.1"
	port = 5000

	s=socket.socket()
	s.bind((host,port))

	s.listen(1)

	c, addr = s.accept()
	print "connected with: "+str(addr)

	while True:
		data = c.recv(1024)
		if not data:
			break
		print "recieved from connection: "+str(data)
		data = str(data).upper()
		encrypted = obj.encrypt(data)
		print "encrypting..."
		print "encrypted data: "+str(encrypted)
		print "sending: "+str(data)
		c.send(encrypted)
	c.close()

if __name__ == "__main__":
	main()
