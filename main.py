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

## AES requires block size to be 16, 24, or 32
## Eventually I'd like a PADDING algorithm here.
plain_text = "stuff"
while len(plain_text)!=16:
    plain_text = raw_input('Please enter 16 characters to be encrypted: ')
    print len(plain_text), " NOPE, try again..."
else:
    print plain_text, " is exactly 16 characters! GREAT JOB!"
    
## Seting up the SSL conection
HSM = raw_input('Please enter the IP address of the machine you are connecting to.')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = ssl.wrap_socket(sock,
    ssl_version=ssl.PROTOCOL_TLSv1,
	keyfile="AKMClientPrivKey.pem", 
	certfile="AKMClientSignedCert.pem", 
	ca_certs="TCASelfSignedCert.pem", 
	cert_reqs=ssl.CERT_REQUIRED)
sslSocket.connect((HSM, 6000))
print "Connection is successful!"
