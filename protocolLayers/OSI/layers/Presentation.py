

from OSI.layers.Session import Session


class Presentation:
    def __init__(self) -> None:
        self.session = Session()

    def send(self,message):
        self.message = self.encode(message)
        return self.session.send(self.message)

    def receive(self,message):
        mes = self.session.receive(message)
        self.message = self.decode(mes)
        return self.message
    
    def encode(self,message):
        mes = 'Presentation '+message
        print('encoding message is: ', mes, ' Length is: ', len(mes))
        return mes

    def decode(self,message):
        mes = message.lstrip('Presentation ')
        print('dencoding message is: ', mes, ' Length is: ', len(mes))
        return mes