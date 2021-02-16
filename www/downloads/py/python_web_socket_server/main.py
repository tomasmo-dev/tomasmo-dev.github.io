'''

    !!!RUN FROM COMMAND LINE!!!

    !!!JPEG IMAGES ONLY ON WEB!!!

'''
import os
import socket
import threading
import time
import sys
import base64

#   Variables

power = True
#   constants
WEB_PAGE_PATH = os.getcwd()

RESPONSE = "HTTP/1.1 200 OK\r\n"

content_type_img = "Content-Type: image/jpeg\r\n"
content_type_html = "Content-Type: text/html\r\n"
content_type_css = "Content-Type: text/css\r\n"
content_type_js = "Content-Type: text/javascript\r\n"

SERVER_IP = "192.168.0.190"
ENCODE_TYPE = "utf-8"
PORT = 8080
ADDR = (SERVER_IP, PORT)

LOG_NAME = ".server_log.txt"
LOG_PATH = os.getcwd()
LOG_PATH = os.path.join(LOG_PATH, LOG_NAME)

#   Log file Open

log = open(LOG_PATH, "a+")

#   Socket Server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def LogPrint(arg, printData=True):
    if printData:
        print(arg)
        log.write(arg + "\n")
        log.flush()
    else:
        log.write(arg + "\n")
        log.flush()

def rcvMsg(sockInstance, header):
    
    recieved = sockInstance.recv(header).decode(ENCODE_TYPE)
    return recieved
        

def GetTime():
    timeTemp = time.localtime(time.time())
    return f"[ {timeTemp.tm_hour}H-{timeTemp.tm_min}m-{timeTemp.tm_sec}s ] "

def server_kill():
    power = False
    LogPrint(GetTime() + "Disconnecting All Users & Shutting Down...")

    log.close()

def handle_client(sockObj, addr):

    LogPrint(GetTime() + "Response data sent to : {}".format(addr))

    request = sockObj.recv(1024).decode(ENCODE_TYPE)
    headers = request.split("\n")
    filename = headers[0].split()[1]


    if filename == "/":
        filename = "/index.html"

    fileType = filename.rsplit(".", 1)[-1]

    if fileType == "jpg" or fileType == "ico":
        fileType = content_type_img

    elif fileType == "css":
        fileType = content_type_css
    
    elif fileType == "html":
        fileType = content_type_html

    elif fileType == "js":
        fileType = content_type_js

    temp = os.path.join(os.getcwd(), "www")

    filename = temp + filename

    try:
        if filename.rsplit(".", 1)[-1] == "ico" or filename.rsplit(".", 1)[-1] == "jpg":

            file = open(filename, "rb")
            content = file.read()
            file.close()

            response = RESPONSE.encode() + fileType.encode() + "\r\n".encode() + content

        else:

            file = open(filename)
            #print(filename)
            content = file.read()
            file.close()
            
            response = RESPONSE + fileType + "\r\n" + content
            response = response.encode()

    except FileNotFoundError as e:
        print(e)
        response = 'HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found'.encode()

    sockObj.sendall(response)
    
    sockObj.close()

def Listen(serverInstance):

    serverInstance.listen()
    LogPrint(GetTime() + "Listening on " + SERVER_IP)
    while power:

        conn, addr = serverInstance.accept()

        handleClient = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        handleClient.start()

        LogPrint(GetTime() + "New connection from {}".format(addr, ))


def Server_Start(ServerInstance):
    LogPrint(GetTime() + "Initiliazing...")

    if power:
        LogPrint(GetTime() + "Sys version             : {}".format(sys.version))
        LogPrint(GetTime() + "Current server Ip       : {}".format(SERVER_IP))
        LogPrint(GetTime() + "Current Port            : {}".format(PORT))

        start_listening = threading.Thread(target=Listen, args=(ServerInstance, ), daemon=True)
        start_listening.start()


starting_Thread = threading.Thread(target=Server_Start, args=(server, ), daemon=True)
starting_Thread.start()
starting_Thread.join()

time.sleep(1)
try:
    while True:
        cmd = str(input("Enter commands :   "))

        if cmd == "EMERG_EXIT":
            sys.exit(1)
        # Commands
        elif cmd == "clear":
            os.system("cls||clear")
finally:
    server_kill()
    print("Done...")
