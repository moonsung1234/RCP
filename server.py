
import load

load.init("./module")

from display import Screen
from packet import Packet
from sk import Server

from threading import Thread
from PIL import Image
import numpy as np
import json
import time

threads = []
client_list = {}
recv_len = 1024 # default
si = input("학급을 입력해주세요 : ")

# set server
server = Server("192.168.219.110", 8080)
server.listen()

# set screen
screen = Screen(1000, 700)

def clickCallback(e) :
    target = screen.combobox.get()

    program_packet = Packet("program", None)
    background_packet = Packet("background", None)

    server.send(program_packet.encode(), client_socket=client_list[target])    
    # time.sleep(0.1)
    server.send(background_packet.encode(), client_socket=client_list[target])

screen.setTitle(si)
screen.setCombobox(clickCallback)
screen.setPicture()
screen.setProgramBar()

def clientCallback(_client_socket, _addr) :
    global recv_len

    while True :
        data = server.receive(recv_len, client_socket=_client_socket)
        p = Packet.decode(data)

        if p.packet == "ip_len" or p.packet == "pp_len" :
            recv_len = p.data

        elif p.packet == "sip" :
            client_list[p.data] = _client_socket

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

def start() :
    while True :
        server.connect()

        print(server.addr)

        client_thread = Thread(target=clientCallback, args=(server.client_socket, server.addr))
        client_thread.daemon = True
        client_thread.start()

        threads.append(client_thread)

        time.sleep(1)

thread = Thread(target=start)
thread.daemon = True
thread.start()

screen.show()