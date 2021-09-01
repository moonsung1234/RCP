
import load

load.init("./module")

from packet import Packet
from sk import Client
import program

from threading import Thread
from PIL import ImageGrab
import numpy as np
import json
import time

# set client
# client = Client("125.182.224.34", 8080)
client = Client("192.168.219.110", 8080)

def getBackgroundImage() :
    img = ImageGrab.grab().resize((650, 350))
    img_list = np.array(img).tolist()

    return img_list

client.connect()

school_info = input("학번을 입력해주세요 : ")

sip_packet = Packet("sip", school_info)
client.send(sip_packet.encode())

def start() :
    while True :
        data = client.receive(1024)
        packet = Packet.decode(data)

        if packet != None and packet.packet == "program" :
            p = json.dumps(program.getVisiableProgram()).encode()

            # send packet length
            pp_packet = Packet("pp", p)
            pp_len_packet = Packet("pp_len", len(pp_packet.encode()))
            
            client.send(pp_len_packet.encode())
            client.send(pp_packet.encode())

            packet = None

        elif packet != None and packet.packet == "background" :
            background = json.dumps(getBackgroundImage())

            # send packet length
            ip_packet = Packet("ip", background)
            ip_len_packet = Packet("ip_len", len(ip_packet.encode()))

            client.send(ip_len_packet.encode())
            client.send(ip_packet.encode())

            packet = None

start()