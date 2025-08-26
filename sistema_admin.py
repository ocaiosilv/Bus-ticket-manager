# As importações continuam as mesmas
from onibus import Onibus, OnibusExecutivo, OnibusConvencional
from passageiro import Passageiro
from viagem import Viagem 

class SistemaAdmin:
    def __init__(self):

        self.__viagens = []
        self.__proximo_id_viagem = 1

    def cadastrar_viagem(self, origem, destino, dias_da_semana, hora, preco_base, tipo_onibus, modelo, fabricante):
        onibus_obj = None
        if tipo_onibus.lower() == 'convencional':
            onibus_obj = OnibusConvencional(modelo, fabricante, 6, "Ônibus convencional com 48 lugares")
        elif tipo_onibus.lower() == 'executivo':
            onibus_obj = OnibusExecutivo(modelo, fabricante, 8, "Ônibus executivo de dois andares")
        else:
            return None

        nova_viagem = Viagem(self.__proximo_id_viagem, origem, destino, dias_da_semana, hora, preco_base, onibus_obj)
        self.__viagens.append(nova_viagem)
        self.__proximo_id_viagem += 1
        
        return nova_viagem

    def buscar_viagem_por_id(self, id_viagem):
        for viagem in self.__viagens:
            if viagem.get_id_viagem() == id_viagem:
                return viagem
        return None
    
    def get_todas_as_viagens(self):
        return self.__viagens
