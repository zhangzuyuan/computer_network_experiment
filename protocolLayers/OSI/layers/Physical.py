

class Physical:
    def __init__(self) -> None:
        self.message = ''

    def send(self,message):
        self.message = self.encode(message)
        return self.message
    
    def receive(self,message):
        self.message = self.decode(message)
        return self.message

    
    def encode(self,message):
        mes = 'Physical '+message
        print('encoding message is: ', mes, ' Length is: ', len(mes))
        return mes

    def decode(self,message):
        mes = message.lstrip('Physical ')
        print('dencoding message is: ', mes, ' Length is: ', len(mes))
        return mes