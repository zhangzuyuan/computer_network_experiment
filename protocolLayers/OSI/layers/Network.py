

from OSI.layers.DataLink import DataLink


class Network:
    def __init__(self) -> None:
        self.datalink = DataLink()

    def send(self,message):
        self.message = self.encode(message)
        return self.datalink.send(self.message)

    def receive(self,message):
        mes = self.datalink.receive(message)
        self.message = self.decode(mes)
        return self.message
    
    def encode(self,message):
        mes = 'Network '+message
        print('encoding message is: ', mes, ' Length is: ', len(mes))
        return mes

    def decode(self,message):
        mes = message.lstrip('Network ')
        print('dencoding message is: ', mes, ' Length is: ', len(mes))
        return mes