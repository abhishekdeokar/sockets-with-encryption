#! /usr/bin/env python3

import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import hashlib
from Crypto.Cipher import AES
import ssl
from ssl import PROTOCOL_TLS

keyFile = "priv.pem"									#provide full path to the private key file location
certFile = "cert.crt"									#provide full path to the Certificate file location

KEY = hashlib.sha256(b"some random password").digest()	#this will convert any pnemonic string which the user wants to choose as password to a 32 bit encrypted object

IV = b"abcdefghijklmnop"								#Initialization vector should always be 16 bit
obj = AES.new(KEY, AES.MODE_CFB, IV)					#creating an object to encrypt our data with

def echo_client(s):
	while True:
		data = s.recv(1024)
		if not data:
			break
		print ("recieved from connection: "+str(data))
		data = data.upper()								#converting the received string t upper case
		encrypted = obj.encrypt(data)					#encrypting the data to be sent using the AES object we created
		print ("encrypting...")
		print ("encrypted data: "+str(encrypted) )
		print ("sending: "+str(data))
		s.send(encrypted)
	s.close()

def main():
	host = "127.0.0.1"
	port = 5001

	s=socket.socket(AF_INET, SOCK_STREAM)				#specifying TCP and IPv4
	s.bind((host,port))									#bind() takes only one argument

	s.listen(1)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	#socket.setsockopt(level, optname, value)
	#level - The level argument specifies the protocol level at which the option resides. To set options at the socket level, specify the level argument as SOL_SOCKET. 
	#optname - SO_REUSEADDR - Specifies that the rules used in validating addresses supplied to bind() should allow reuse of local addresses, if this is supported by the protocol. This option takes an int value. This is a Boolean option.
	#value -  The value can be an integer or a string representing a buffer.
	s_ssl=ssl.wrap_socket(s, keyfile=keyFile, certfile=certFile, server_side=True)
	#the above function "wraps" the socket created with the security layer of signed certificate, private key
	#The parameter server_side is a boolean which identifies whether server-side or client-side behavior is desired from this socket, true specifies server behaviour.
	while True:
		try:
			c, addr = s_ssl.accept()
			print ("connected with: "+str(addr))
			echo_client(c)
		except socket.error as e:
			print ("Error:{0}".format(e))

if __name__ == "__main__":
	main()