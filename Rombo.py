from Forma import Forma

class Rombo(Forma):
    
    def __init__(self):
        super().__init__()
        self.orientaciones["noreste"] = None
        self.orientaciones["sureste"] = None
        self.orientaciones["suroeste"] = None
        self.orientaciones["noroeste"] = None