
# TCP Sockets with AES and SSL

This example is an implementation of Socket Programming with addition of SSL and AES implementations using Python. 

Requirements for this implementation are a private key and a server certificate generated using the private key, both of which can be generated using openssl. The `key_cert_gen.sh` file is a script to generate the keys and certificates that will be required to form the SSL connection. The script prompts to enter password used for generating the private key multiple times.

The inner layer is of AES encryption. The data to be sent is encrypted and decrypted using AES objects.

The outer layer is of SSL. The method ssl.wrap_socket() will wrap the socket with the required security considerations. In this example, only a key and a self signed certificate have been provided to ssl.wrap_socket(), and the other options have been left which are automatically set as default. This is however not recommended in Python documentation and the other options should be configured for better security.

This is a rudimentary code to start a channel between a server and a client, the client sends a certain message which is received by the server and the server then simply sends back the case converted message.

### Usage :-
1. Change File permissions in the directory<br>
	`sudo chmod +x key_cert_gen.sh *.py`

2. Run the Key and Certificate generator<br>
	`./key_cert_gen.sh`

3. In one terminal<br>
	`./tcpServer.py`

4. In another terminal<br>
	`./tcpClient.py`

From the client terminal, you can then send any string, if it contains small case letters, they will be converted to upper case on the server side and sent back to the client.

### References :-

1. Sockets implementation:<br>
	https://www.youtube.com/watch?v=XiVVYfgDolU&t=2s

2. AES encryption guidepoints:<br>
	https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto

3. Key and Certificate generation:<br>
	Ivan Ristić OpenSSL Cookbook A guide to the most frequently used OpenSSL features and commands

4. Implementing SSL in sockets:<br>
	http://grantcurell.com/2017/03/10/a-simple-ssl-client-and-server-in-python/

