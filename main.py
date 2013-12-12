# Crypto.Cipher is a module that is part of PyCrypto
# https://www.dlitz.net/software/pycrypto  This must be installed
# for this code to function properly

from Crypto.Cipher import AES
import base64
import os
import socket, ssl
import hashlib

## AES requires block size to be a multiple of 16, 24, or 32
blockSize = 16
padding = '#'
pad = lambda s: s + (blockSize - len(s) % blockSize) * padding

encode = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
decode = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(padding)

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
print "First we will generate some data."


plain_text = raw_input('Please enter your name: ')
#secret_text = plain_text.rjust(blockSize, '0')



print "Your input after padding/hashing:", plain_text

#
### Set up the SSL conection
#

HSM = raw_input('Please enter the IP address of the machine you are connecting to[192.168.160.128]:      ')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = ssl.wrap_socket(sock,
    ssl_version=ssl.PROTOCOL_TLSv1,
	keyfile="AKMClientPrivKey.pem", 
	certfile="AKMClientSignedCert.pem", 
	ca_certs="TCASelfSignedCert.pem", 
	cert_reqs=ssl.CERT_REQUIRED)
sslSocket.connect((HSM, 6000))
print "Connection OPENED"

# Send request
sslSocket.write("000712001Key01-128                               " \
	"                        BIN");

# Read response
full_response = ""
response = sslSocket.read()
while response:
	full_response += response
	response = sslSocket.read()

# Close the connection
sslSocket.close()
print "Connection CLOSED"

key = hashlib.sha256(full_response).digest()
print 'Encryption Key:', key

# Create a cipher object using the hashed response
cipher = AES.new(key)

# Encrypt and encode a string
encrypt = encode(cipher, plain_text)
print 'EEncrypted String:', encrypt

# Decrypt and decode the encoded string
decrypt = decode(cipher, encrypt)
print 'Decrypted string:', decrypt
