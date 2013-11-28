import os
import socket
import ssl

# HSM = raw_input('Please enter the IP address of the machine you are connecting to.')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = ssl.wrap_socket(sock, 
	keyfile="AKMClientPrivateKey.pem", 
	certfile="AKMClientSignedCert.pem", 
	ca_certs="TCASelfSignedCert.pem", 
	cert_reqs=ssl.CERT_REQUIRED)
sslSocket.connect(('192.168.160.128', 6000))
print "Connection is successful!"