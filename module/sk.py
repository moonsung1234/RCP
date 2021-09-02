
import socket

class Server :
    def __init__(self, host, port) :
        self.host = host
        self.port = port

    def listen(self) :
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

    def connect(self) :
        self.client_socket, self.addr = self.server_socket.accept()

        return self.client_socket, self.addr

    def receive(self, buffer_size, client_socket=None) :
        if client_socket != None :
            return client_socket.recv(buffer_size)

        else :
            return self.client_socket.recv(buffer_size)

    def send(self, data, client_socket=None) :
        if client_socket != None :
            return client_socket.sendall(data)

        else :
            return self.client_socket.sendall(data)

    def closeServer(self) :
        self.server_socket.close()
    
    def closeClient(self) :
        self.client_socket.close()

class Client(Server) :
    def __init__(self, host, port):
        super().__init__(host, port)

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port)) 

    def receive(self, buffer_size):
        return super().receive(buffer_size)

    def send(self, data) :
        return super().send(data)