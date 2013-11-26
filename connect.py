HSM = raw_input('Please enter the IP address of the machine you are connecting to.')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = ssl.wrap_socket(sock, 
	keyfile="./CA/AKMClientPrivateKey.pem", 
	certfile="./CA/AKMClientSignedCert.pem", 
	ca_certs="./CA/TCASelfSignedCert.pem", 
	cert_reqs=ssl.CERT_REQUIRED)
sslSocket.connect((HSM, 6000))
print "Connection is successful!"