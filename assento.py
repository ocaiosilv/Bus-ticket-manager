class Assento:
    def __init__(self,numero,ocupado):
        self.__numero = numero
        self.__ocupado = ocupado
        self.__passageiro = None

    def get_numero(self):
        return self.__numero
    
    def set_numero(self,numero):
        self.__numero = numero
    
    def get_ocupado(self):
        return self.__ocupado

    def set_ocupado(self, ocupado):
        self.__ocupado = ocupado
    
    def get_passageiro(self):
        return self.__passageiro

    def set_passageiro(self, passageiro):
        self.__passageiro = passageiro

    