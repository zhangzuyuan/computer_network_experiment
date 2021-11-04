

from OSI.layers.Network import Network


class Transport:
    def __init__(self) -> None:
        self.network = Network()

    def send(self,message):
        self.message = self.encode(message)
        return self.network.send(self.message)

    def receive(self,message):
        mes = self.network.receive(message)
        self.message = self.decode(mes)
        return self.message
    
    def encode(self,message):
        mes = 'Transport '+message
        print('encoding message is: ', mes, ' Length is: ', len(mes))
        return mes

    def decode(self,message):
        mes = message.lstrip('Transport ')
        print('dencoding message is: ', mes, ' Length is: ', len(mes))
        return mes