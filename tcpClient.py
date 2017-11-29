import socket
from Crypto.Cipher import AES

obj = AES.new("this is a key123",AES.MODE_CFB,"abcdefghijklmnop")

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
