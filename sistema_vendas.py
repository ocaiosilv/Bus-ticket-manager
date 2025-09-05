# sistema_vendas.py
from passageiro import Passageiro
from passagem import Passagem

class SistemaVendas:
    def __init__(self, lista_de_viagens_principal):
        self.lista_viagens = lista_de_viagens_principal
    
    def buscar_viagens_disponiveis(self, origem, destino):
        encontradas = []
        for viagem in self.lista_viagens:
            if viagem.get_origem().lower() == origem.lower() and viagem.get_destino().lower() == destino.lower():
                encontradas.append(viagem)
        return encontradas

    def vender_passagem(self, viagem, dados_passageiro, tipo_assento, linha, coluna):
        passageiro = Passageiro(
            dados_passageiro['nome'],
            dados_passageiro['idade'],
            dados_passageiro['cpf'],
            dados_passageiro['email'],
            dados_passageiro['telefone'],
            dados_passageiro['pcd']
        )
        
        onibus = viagem.get_onibus()
        sucesso = onibus.ocupar_assento(tipo_assento, linha, coluna, passageiro)

        if not sucesso:
            return (False, "Assento inválido ou já ocupado.")
            
        preco_final = viagem.preco_base
        if tipo_assento == "Leito":
            preco_final *= 1.5
        if passageiro.eh_isento_de_pagamento():
            preco_final = 0.0

        assento_str = f"{tipo_assento} F{linha+1}-P{coluna+1}"
        passagem = Passagem(viagem.get_origem(), viagem.get_destino(), passageiro, assento_str, preco_final)
        
        return (True, passagem)