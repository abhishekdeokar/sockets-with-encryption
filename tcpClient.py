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

	s.connect((host,port))

	message = raw_input("-> ")
	while message != 'q':
		s.send(message)
		data = s.recv(1024)
		print "received data: "+str(data)
		print "decrypting..."
		decrypted = obj.decrypt(data)
		print "received from server "+str(decrypted)
		message = raw_input("-> ")

	s.close()

if __name__ == "__main__":
	main()
