# super simple way to connect to a web service via a socket in python - below is a super simple web browser
import socket
 #these arguments basically say - connect over the internet, and the data is a stream
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#these arguments the host to connect to, and the port to use.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#note- .encode will by default encode in utf-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # note - have to decode when you receive the data
    print(data.decode(),end='')
mysock.close()