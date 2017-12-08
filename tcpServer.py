import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import hashlib
from Crypto.Cipher import AES
import ssl
from ssl import PROTOCOL_TLS

keyFile = "privateKey.pem"	#provide full path to the private key file location
certFile = "sslCert.crt"	#provide full path to the Certificate file location

KEY = hashlib.sha256("some random password").digest()

IV = "abcdefghijklmnop"
obj = AES.new(KEY, AES.MODE_CFB, IV)

def echo_client(s):
	while True:
		data = s.recv(1024)
		if not data:
			break
		print "recieved from connection: "+str(data)
		data = str(data).upper()
		encrypted = obj.encrypt(data)
		print "encrypting..."
		print "encrypted data: "+str(encrypted)
		print "sending: "+str(data)
		s.send(encrypted)
	s.close()

def main():
	host = "127.0.0.1"
	port = 5001

	s=socket.socket(AF_INET, SOCK_STREAM)
	s.bind((host,port))

	s.listen(1)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	
	s_ssl=ssl.wrap_socket(s, keyfile=keyFile, certfile=certFile, server_side=True)
	while True:
		try:
			c, addr = s_ssl.accept()
			print "connected with: "+str(addr)
			echo_client(c)
		except socket.error as e:
			print "Error:{0}".format(e)

if __name__ == "__main__":
	main()
