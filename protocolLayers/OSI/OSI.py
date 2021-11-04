
from .layers.Application import Application

class OSI:
    def __init__(self) -> None:
        self.application = Application()

    def send(self,message):
        return self.application.send(message)
    
    def receive(self,message):
        return self.application.receive(message)