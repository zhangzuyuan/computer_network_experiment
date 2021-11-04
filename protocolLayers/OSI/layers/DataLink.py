
from OSI.layers.Physical import Physical


class DataLink:
    def __init__(self) -> None:
        self.physical = Physical()

    def send(self,message):
        self.message = self.encode(message)
        return self.physical.send(self.message)
    
    def receive(self,message):
        mes = self.physical.receive(message)
        self.message = self.decode(mes)
        return self.message

    
    def encode(self,message):
        mes = 'DataLink '+message
        print('encoding message is: ', mes, ' Length is: ', len(mes))
        return mes

    def decode(self,message):
        mes = message.lstrip('DataLink ')
        print('dencoding message is: ', mes, ' Length is: ', len(mes))
        return mes
    