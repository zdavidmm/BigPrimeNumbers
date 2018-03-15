import socket
import random as r
host = socket.gethostname()
port = 10256                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

num = r.getrandbits(100)
numIsPrime = False
while numIsPrime == False:
    s.sendall(str(num))
    data = s.recv(1024)

    if data == "False":
        num = num + 1
        print "Adding 1 to try and make the number prime!"
    if data == "True":
        print "The prime number is " + str(num)
        break
