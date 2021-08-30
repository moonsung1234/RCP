
from threading import Thread
from PIL import ImageGrab
from sk import Client
import numpy as np
import program
import json
import time

# packet = ""
data = ""

# set client
# client = Client("125.182.224.34", 8080)
client = Client("192.168.219.110", 8080)

def getBackgroundImage() :
    img = ImageGrab.grab().resize((650, 350))
    img_list = np.array(img).tolist()

    return json.dumps(img_list).encode()

client.connect()

school_info = input("학번을 입력해주세요 : ")

client.send(b"sips") # school information packet start
client.send(school_info.encode())
client.send(b"sipe") # school information packet end

def handleBackground() :
    global data

    while True :
        if data == "background" :
            client.send(b"ips") # image packet start
            client.send(getBackgroundImage())
            client.send(b" " * 1000) # flush
            client.send(b"ipe") # image packet end

            data = ""

        time.sleep(1)

def handleProgram() :
    global data

    while True :
        if data == "program" :
            client.send(b"pps") # program packet start
            client.send(json.dumps(program.getVisiableProgram()).encode())
            client.send(b" " * 1000) # flush
            client.send(b"ppe") # program packet end

            data = ""

        time.sleep(1)

def start() :
    thread1 = Thread(target=handleBackground)
    thread1.daemon = True
    thread1.start()

    thread2 = Thread(target=handleProgram)
    thread2.daemon = True
    thread2.start()

    global data

    while True :
        data = client.receive(1024).decode().strip()

start()