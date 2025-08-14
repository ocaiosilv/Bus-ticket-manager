from passageiro import Passageiro
import random
class Passagem:
    def __init__(self,saida,destino,passageiro,assento,preco):
        self.__saida = saida
        self.__destino = destino
        self.__passageiro = passageiro
        self.__bilhete = str(random.randint(100000,999999))
        self.__assento = assento
        self.__preco = preco
        
    def get_saida(self):
        return self.__saida

    def set_saida(self, saida):
        self.__saida = saida

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_passageiro(self):
        return self.__passageiro

    def set_passageiro(self, passageiro):
        self.__passageiro = passageiro

    def get_bilhete(self):
        return self.__bilhete

    def set_bilhete(self, bilhete):
        self.__bilhete = bilhete

    def get_assento(self):
        return self.__assento

    def set_assento(self, assento):
        self.__assento = assento

    def get_preco(self):
        return self.__preco
    
    def set_preco(self,preco):
        self.__preco = preco
