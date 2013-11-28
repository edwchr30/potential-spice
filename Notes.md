Notes
================

I created this to document the work that I'm doing:
1. Writing Code
2. Research
3. Setup

I should have started earlier, but I wont back date.
If my memory was perfect, I wouldn't have to write
this all down.

11/27/2013
----------------
More troubleshooting, I got all of my certs in order.
Still dealing with this error.

>Traceback (most recent call last):
>  File "connect.py", line 12, in <module>
    sslSocket.connect(['192.168.160.128', 6000])
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ssl.py", line 333, in connect
    self._real_connect(addr, False)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ssl.py", line 314, in _real_connect
>    self.ca_certs, self.ciphers)
>ssl.SSLError: [Errno 336265218] _ssl.c:351: error:140B0002:SSL >routines:SSL_CTX_use_PrivateKey_file:system lib

I've put it up on stackoverflow.com
http://stackoverflow.com/questions/20256023/unable-to-connect-to-socket-using-ssl-and-python-feeling-lost

11/26/2013
----------------
Spent the evening diggin' through stack overflow and getting the Hardware Security Module Virtual Machine configured properly.

11/25/2013
----------------
Researched and played around trying to get my ssl syntax working properly.

11/22/2013
----------------
Got my input loop functioning properly
  Mostly syntax error, which was much easier to 
  figure out one I stopped reading all about it
  and just did some debugging.

Read 
  http://bobthegnome.blogspot.com/2007/08/making-ssl-connection-in-python.html
  http://stackoverflow.com/questions/12336239/how-to-open-ssl-socket-using-certificate-stored-in-string-variables-in-python
  http://docs.python.org/2/library/ssl.html#ssl.wrap_socket
  
Setting up a Hardware Security Module in VMware
