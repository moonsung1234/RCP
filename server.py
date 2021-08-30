
from threading import Thread
from display import Screen
from sk import Server
from PIL import Image
import numpy as np
import json
import time

client_list = {}
threads = []
is_upload = False
upload_delay = 2

packet = ""
data = ""

# set server
server = Server("192.168.219.110", 8080)
server.listen()

# set screen
screen = Screen(1000, 700)

def clickCallback(e) :
    if not is_upload :
        target = screen.combobox.get()

        # thread = Thread(target=loadCallback, target=(list[target],))
        # thread.daemon = True
        # thread.start()

        server.send(b"program", client_socket=client_list[target])

        time.sleep(1)

        server.send(b"background", client_socket=client_list[target])

    else :
        print("Another work is doing...")

screen.setTitle("<2학년 7반>")
screen.setCombobox(clickCallback)
screen.setPicture()
screen.setProgramBar()

def clientCallback(_client_socket, _addr) :
    global packet
    global data

    image = ""
    program = ""

    while True :
        data = server.receive(1024, client_socket=_client_socket).decode().strip()

        if data == "sips" :
            packet = "sip"

        elif data == "ips" :
            packet = "ip"

        elif data == "pps" :
            packet = "pp"

        if packet == "sip" :
            if data == "sipe" :
                packet = ""

            else :
                if not data == "sips" :
                    client_list[data] = _client_socket

                    screen.addElement(data)

        elif packet == "ip" :
            if data == "ipe" :
                img = Image.fromarray(np.array(json.loads(image)).astype(np.uint8))
                img.save("./background.png")

                screen.updatePicture()

                packet = ""
                image = ""

                print("upload success!")

            else :
                if not data == "ips" :
                    image += data

        elif packet == "pp" :
            if data == "ppe" :
                p_list = json.loads(program)

                screen.program_bar.delete(1.0, screen.tk.END)

                for p in list(reversed(p_list)) :
                    screen.program_bar.insert(1.0, "-   " + p + "\n\n")

                screen.program_bar.insert(1.0, "\n\n")
                
                packet = ""
                program = ""

                print("getting program success!")
            
            else :
                if not data == "pps" :
                    program += data

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