# Crypto.Cipher is a module that is part of PyCrypto
# https://www.dlitz.net/software/pycrypto  This must be installed
# for this code to function properly

from Crypto.Cipher import AES
import base64
import os
import socket, ssl

##Title##
print "This program serves to demonstrate"
print "that encryption offers protection"
print "beyond intrusion prevention.  With"
print "encryption and properly managed"
print "keys, you can protect your data"
print "even if it gets stolen/misplaced."
print "\n"
print "The steps will be explained as"
print "we go."
print "\n"
print "First we will create a file."

## AES requires block size to be a multiple of 16, 24, or 32
blockSize = 16

## get input from the user and pad it up to a compatible size
plain_text = raw_input('Please enter your name: ')
secret_text = plain_text.rjust(blockSize, 'Z')

print "You padded input", secret_text
## Seting up the SSL conection
##HSM = raw_input('Please enter the IP address of the machine you are connecting to.')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = ssl.wrap_socket(sock,
    ssl_version=ssl.PROTOCOL_TLSv1,
	keyfile="AKMClientPrivKey.pem", 
	certfile="AKMClientSignedCert.pem", 
	ca_certs="TCASelfSignedCert.pem", 
	cert_reqs=ssl.CERT_REQUIRED)
sslSocket.connect((192.168.160.128, 6000))
print "Connection is successful!"

# Send request to AKM
sslSocket.write("000712001Key01-128                               " \
	"                        BIN");

# Read response from AKM
full_response = ""
response = sslSocket.read()
while response:
	full_response += response
	response = sslSocket.read()

# Close the connection to AKM
sslSocket.close()

print full_response

