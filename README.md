This example is an implementation of Socket Programming with addition of SSL and AES implementations. 

Requirements for this implementation are a private key and a server certificate generated using the private, both of which can be generated using openssl.

The inner layer is of AES encryption. The data to be sent is encrypted and decrypted using AES objects.

The outer layer is of SSL. The method ssl.wrap_socket() will wrap the socket with the required security considerations. In this example, only a key and a self signed certificate have been provided to ssl.wrap_socket(), and the other options have been left which are automatically set as default. This is however not recommended in Python documentation and the other options should be configured for better security.

References: 1. http://grantcurell.com/2017/03/10/a-simple-ssl-client-and-server-in-python/
	    2. https://www.youtube.com/watch?v=XiVVYfgDolU&t=2s
	    3. https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
