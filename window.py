
import load

load.init("./module")

from display import Screen
from packet import Packet
from sk import Client

from threading import Thread
from PIL import Image
import numpy as np
import json
import time

si = input("학급을 입력해주세요 : ")

# set client
# client = Client("125.182.224.34", 8080)
client = Client("192.168.219.110", 8080)
client.connect()

handshake_packet = Packet("window_handshake", si)
client.send(handshake_packet.encode())

# set screen
screen = Screen(1000, 700)

def clickCallback(e) :
    target = screen.combobox.get()

    target_packet = Packet("target", target)
    program_packet = Packet("program", None)
    background_packet = Packet("background", None)

    client.send(target_packet.encode())
    client.send(program_packet.encode())

    time.sleep(1)

    client.send(background_packet.encode())

screen.setTitle(si)
screen.setCombobox(clickCallback)
screen.setPicture()
screen.setProgramBar()

def start() :
    recv_len = 1024 # default

    while True :
        data = client.receive(recv_len)
        p = Packet.decode(data)

        if p.packet == "ip_len" or p.packet == "pp_len" :
            recv_len = p.data

        elif p.packet == "sip" :
            screen.addElement(p.data)

        elif p.packet == "ip" :
            img = Image.fromarray(np.array(json.loads(p.data)).astype(np.uint8))
            img.save("./background.png")

            screen.updatePicture()

        elif p.packet == "pp" :
            p_list = json.loads(p.data)

            screen.program_bar.delete(1.0, screen.tk.END)

            for program in list(reversed(p_list)) :
                screen.program_bar.insert(1.0, "-   " + program + "\n\n")

            screen.program_bar.insert(1.0, "\n\n")

screen.addElement("20707")

thread = Thread(target=start)
thread.daemon = True
thread.start()

screen.show()