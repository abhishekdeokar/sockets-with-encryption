import socket
import hashlib
from Crypto.Cipher import AES
import ssl

KEY = hashlib.sha256("some random password").digest()

IV = "abcdefghijklmnop"
obj = AES.new(KEY, AES.MODE_CFB, IV)

def main():
	host = "127.0.0.1"
	port = 5001

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	ssl_sock = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/home/maverick/Practice/Socket_Prog/key_cert/sslCert.crt')

	ssl_sock.connect((host,port))

	message = raw_input("-> ")
	while message != 'q':
		#s.send(message)
		ssl_sock.write(message)
		data = ssl_sock.recv(1024)
		print "received data: "+str(data)
		print "decrypting..."
		decrypted = obj.decrypt(data)
		print "received from server "+str(decrypted)
		message = raw_input("-> ")

	ssl_sock.close()

if __name__ == "__main__":
	main()
