from socket import *
import time

serverName = 'localhost'
#serverName = 'google.com'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
ping = bytes("PING", "utf-8")

# this function will send a message to server and return
# ping time if the server responses, return None if server
# does not reponse 
def ping_server():
    # using settimeout socket's built-in function 
    clientSocket.settimeout(1)
    # while not timeout
    try:
        start = time.perf_counter()
        clientSocket.sendto(ping,(serverName, serverPort))
        response, serverAddress = clientSocket.recvfrom(2048)
        end = time.perf_counter()
        return end-start
    # when timeout
    except timeout:
        return None

# main function will ping to server 10 times and calculate
# the avg ping time
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
    print('There are ' + str(success) + ' success packet')
    
raw_input()
clientSocket.close()


