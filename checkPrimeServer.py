import socket
import time
import random as r

def isPrime(n, k=5): # miller-rabin
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2
    for i in range(k):
        x = pow(r.randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for k in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

if __name__ == '__main__':
    host = ''        # Symbolic name meaning all available interfaces
    port = 10256     # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    print host , port
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    isNumPrime = False
    while isNumPrime == False:
        try:
            data = conn.recv(6000)
            if data:
                print "Checking if " + data + " is prime!"
                checkNum = int(data)
                isNumPrime = isPrime(checkNum)
                if isNumPrime == False:
                    print "It is not :("
                else:
                    print "It is! :)"

                conn.sendall(str(isNumPrime))
        except socket.error:
            print "Error Occured."
            conn.sendall("Error")

    print "Closing connection..."
    conn.close()
