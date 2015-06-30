from socket import *
import time

serverName = 'localhost'
#serverName = 'google.com'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

ping = bytes("PING", "utf-8")


def ping_server():
    clientSocket.settimeout(1)
    try:
        start = time.perf_counter()
        clientSocket.sendto(ping,(serverName, serverPort))
        response, serverAddress = clientSocket.recvfrom(2048)
        end = time.perf_counter()
        return end-start
    except timeout:
        return None

sum = 0
success = 0
for i in range(1,11):
    temp = ping_server()
    if temp == None:
        print('packet ' + str(i) + ' lost')
    else:
        print('packet ' + str(i) +' RTT = ' + str(temp) + ' seconds')
        sum += ping_server()
        success += 1
if(success !=0):
    print('Avg ping time = ' + str(sum/success) + ' seconds')
    

clientSocket.close()


