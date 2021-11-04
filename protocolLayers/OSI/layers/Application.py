
from OSI.layers.Presentation import Presentation


class Application:
    def __init__(self) -> None:
        self.presentation = Presentation()
    
    def send(self,message):
        self.message = self.encode(message)
        return self.presentation.send(self.message)
    
    def receive(self,message):
        mes = self.presentation.receive(message)
        self.message = self.decode(mes)
        return self.message

    
    def encode(self,message):
        mes = 'Application '+message
        print('encoding message is: ', mes, ' Length is: ', len(mes))
        return mes

    def decode(self,message):
        mes = message.lstrip('Application ')
        print('dencoding message is: ', mes, ' Length is: ', len(mes))
        return mes
    
