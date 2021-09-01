
import pickle

class Packet :
    def __init__(self, packet, data) :
        self.packet = packet
        self.data = data

    def encode(self) :
        return pickle.dumps(self)

    @classmethod
    def decode(self, data) :
        return pickle.loads(data)