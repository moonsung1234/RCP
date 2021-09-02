
# many to one 구조

# -------------------------------------

# window 프로그램에 다수의 클라이언트 프로그램 연결시키기
# 프로그램 구분은 학급으로
# 클라이언트 패킷과 window 패킷을 구분해, 서로 연결시키기
# 클라이언트 패킷이 들어오면 타겟을 확인하고 해당 window 로 전송하기
# window 패킷이 들어오면 타겟을 확인하고 해당 클라이언트로 전송하기
# 클라이언트 소켓과 window 소켓을 분리해놓기
# 스레드는 한 window 당 하나씩 할당하기
# 한 스레드당 연결되어있는 클라이언트들을 담당하기

import load

load.init("./module")

from display import Screen
from packet import Packet
from sk import Server

from threading import Thread
import numpy as np
import json
import time

window_list = {}
recv_len = 1024 # default

# set server
server = Server("192.168.219.110", 8080)
server.listen()

def clientCallback(data) :
    global recv_len

    window = window_list[data]

    while True :
        d = server.receive(recv_len, client_socket=window["socket"])
        p = Packet.decode(d)

        if p.packet == "target" :
            client = list(filter(lambda x : x["data"] == p.data, window["clients"]))[0]
            
        else :
            # program packet & background packet
            for _ in range(2) :
                to_client_packet = Packet(p.packet, p.data)
                server.send(to_client_packet.encode(), client_socket=client["socket"])

                d = server.receive(recv_len, client_socket=client["socket"])
                p = Packet.decode(d)

                if p.packet == "ip_len" or p.packet == "pp_len" :
                    recv_len = p.data

                to_window_packet = Packet(p.packet, p.data)
                server.send(to_window_packet.encode(), client_socket=window["socket"])

def start() :
    while True :
        server.connect()

        print(server.addr)

        data = server.receive(1024)
        p = Packet.decode(data)

        if p.packet == "window_handshake" :
            window_list[p.data] = {
                "socket" : server.client_socket,
                "clients" : []
            }

            thread = Thread(target=clientCallback, args=(p.data,))
            thread.daemon = True
            thread.start()

        elif p.packet == "client_handshake" :
            data2 = server.receive(1024)
            p2 = Packet.decode(data2)

            window_list[p.data]["clients"].append({
                "socket" : server.client_socket,
                "data" : p2.data
            })

start()