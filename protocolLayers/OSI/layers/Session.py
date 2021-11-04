

from OSI.layers.Transport import Transport


class Session:
    def __init__(self) -> None:
        self.transport = Transport()

    def send(self,message):
        self.message = self.encode(message)
        return self.transport.send(self.message)

    def receive(self,message):
        mes = self.transport.receive(message)
        self.message = self.decode(mes)
        return self.message
    
    def encode(self,message):
        mes = 'Session '+message
        print('encoding message is: ', mes, ' Length is: ', len(mes))
        return mes

    def decode(self,message):
        mes = message.lstrip('Session ')
        print('dencoding message is: ', mes, ' Length is: ', len(mes))
        return mes