from socket import *
import time
import os

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
    # set timeout 0.00001 second for testing 
    clientSocket.settimeout(0.00001) 
    # while not timeout
    try:
        start = time.perf_counter()
        clientSocket.sendto(ping,(serverName, serverPort))
        response, serverAddress = clientSocket.recvfrom(2048)
        end = time.perf_counter()
        return end-start
    # if timeout
    except timeout:
        return None

# main function will ping to server until user shutdowns the program
sum = 0
success = 0
i = 0
while 1:
    i += 1
    temp = ping_server()
    if temp == None:
        os.system('cls')
        print('Packet ' + str(i) + ' lost')
    else:
        os.system('cls')
        print('Packet ' + str(i) +' RTT = ' + str(round(temp,5)) + ' seconds')
        sum += ping_server()
        success += 1
        print('Avg ping time = ' + str(round(sum/success,5)) + ' seconds')
        print('Success ping rate = ' + str(round((success*100/i),5)) + '%')
      
clientSocket.close()


