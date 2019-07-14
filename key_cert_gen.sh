#!/bin/sh

openssl genrsa -aes256 -out priv.pem 4096
cat priv.pem
openssl rsa -text -in priv.pem
openssl rsa -in priv.pem -pubout -out pub.pem

openssl req -new -key priv.pem -out cert.csr
openssl req -text -in cert.csr -noout
openssl x509 -req -days 365 -in cert.csr -signkey priv.pem -out cert.crt