from socket import *
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

ping = bytes("PING", "utf-8")


def ping_server():
    start = time.perf_counter()
    clientSocket.sendto(ping,(serverName, serverPort))
    response, serverAddress = clientSocket.recvfrom(2048)
    end = time.perf_counter()
    print('RTT = ' + str(end - start) + ' seconds')
    return end-start

sum = 0
for i in range(0,10):
    sum += ping_server()

print('Avg ping time = ' + str(sum/10) + ' seconds')
    
# keep track time
#start = time.perf_counter()
#clientSocket.sendto(ping,(serverName, serverPort))
#response, serverAddress = clientSocket.recvfrom(2048)
#end = time.perf_counter()
# print the Round Trip Time (RTT)
#print('RTT = ' + str(end - start) + ' seconds')
clientSocket.close()


