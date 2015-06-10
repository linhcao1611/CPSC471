from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    ping, clientAddress = serverSocket.recvfrom(2048)
    response = bytes("PONG", "utf-8")
    serverSocket.sendto(response, clientAddress)
