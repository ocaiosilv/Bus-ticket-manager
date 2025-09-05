from passageiro import Passageiro
from viagem import Viagem
import random

class Passagem:
    def __init__(self, viagem: Viagem, passageiro: Passageiro, assento):
        self.__viagem = viagem
        self.__passageiro = passageiro
        self.__assento = assento
        self.__preco = self.gera_preco()
        self.__bilhete = str(random.randint(1, 999999))

    def get_viagem(self):
        return self.__viagem

    def set_viagem(self, viagem):
        self.__viagem = viagem

    def get_passageiro(self):
        return self.__passageiro

    def set_passageiro(self, passageiro):
        self.__passageiro = passageiro

    def get_assento(self):
        return self.__assento

    def set_assento(self, assento):
        self.__assento = assento

    def get_preco(self):
        return self.__preco

    def get_bilhete(self):
        return self.__bilhete

    def gera_preco(self):
        preco_base = self.__viagem.get_preco()
        if self.__passageiro.eh_isento_de_pagamento():
            return 0.0
        # Ajustes podem ser feitos por tipo de assento se necessário
        return preco_base
