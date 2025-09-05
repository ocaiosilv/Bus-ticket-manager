# sistema_vendas.py
from passageiro import Passageiro
from passagem import Passagem
from onibus_convencional import OnibusConvencional
from onibus_executivo import OnibusExecutivo

# Aqui mudou um monte sei nem explicar, sei que adicionei umas parada, adicionei a troca la, ai adicionei a venda direito
# ai chegou uma hr que tava funcionando, ai parou, ai quando fui adicionando votão, foi ficando uma bagunça, ai pedi pro gepeto 
#ajeitar, ai ficou assim, mas ta daora, da pra entender bem, os gets se elencam com as paradas que passam no main, ai fica tudo bonitinho
# tudo aqui é referente ao main, tipo, no sentido de passar tlgd, nos busca de la, e passa pra ca
""" --- cansei de colocar #
ai ficou basicamente assim
- ajuste na venda de passagens: agora funciona pra convencional e executivo, com seleção de assento em grid
- executivo mostra semi-leito em cima e leito embaixo, cores indicam ocupação
- adicionei a função de troca de passagem 
- integração melhor entre main, sistema_vendas, passagem e ônibus, garantindo que os dados (assento, tipo, linha/coluna) passem corretamente
- e é isso, tem que adicionar o preço que muda, do jeito que tu quer, agora assim, vc que adicione a parada da data, mto dificil

provavelmente vai ter que criar mais um .py, se pa da pra botar uma biblioteca disso, mas ai ne, eu ja n sei se o professor deixa, pq o tktinker que a gente usou
é meio que nativo por assim dizer

- dai tbm, tem que criar a parada de ao pesquisar por viagem, dar pra selecionar uma, ai ver os assentos, ai também, se selecionar os assentos, vem um popup de informação, tipo, ah, assento de xxxx, codigo tal,bla bla bla, 
pq ai ja tem o uso do imprime() de viagem

- ai os raises ne, tem que adicionar pra coisa pra krl, -> se o cpf é o mesmo( email nome, telefone pode ser o mesmo, pode ser de familia), ai raise pra se o nome for invalido, cpf invalido( - de 11 digitos), email invalido, 
sem o @, raise pra hora errada, inclusive, dava pra colocar hora pra ser tipo, um selecionador de hora, mas nao sei fazer isso e talvez nao compense o esforço. raise pra nao colocounada, substituir as coisas que tem return x
pra raise, mas ai eu acho que vai parar o programa n sei, veja ai :)

é isso acho, editar informação da pessoa talvez, mas ai fica mto repetitivo, AH

TEM que fazer o log, TEM PRECISA, pq ta no nosso planejamento do projeto

"""
 

class SistemaVendas:
    def __init__(self, lista_de_viagens):
        self.__lista_viagens = lista_de_viagens
        self.__passagens = []

    def buscar_viagens_disponiveis(self, origem, destino):
        encontradas = []
        for viagem in self.__lista_viagens:
            if viagem.get_origem().lower() == origem.lower() and viagem.get_destino().lower() == destino.lower():
                encontradas.append(viagem)
        return encontradas

    def vender_passagem(self, viagem, dados_passageiro, tipo_assento=None, linha=None, coluna=None):
        passageiro = Passageiro(
            dados_passageiro['nome'],
            dados_passageiro['idade'],
            dados_passageiro['cpf'],
            dados_passageiro.get('email', ''),
            dados_passageiro.get('telefone', ''),
            dados_passageiro.get('pcd', False)
        )

        onibus = viagem.get_onibus()
        sucesso = False
        assento_str = ""

        # Convencional
        if isinstance(onibus, OnibusConvencional):
            numero_assento = dados_passageiro.get('assento', '').strip()
            if not numero_assento:
                return (False, "Assento deve ser informado para ônibus Convencional")
            sucesso = onibus.set_assentos(numero_assento, passageiro)
            assento_str = numero_assento

        # Executivo
        elif isinstance(onibus, OnibusExecutivo):
            if tipo_assento is None or linha is None or coluna is None:
                return (False, "Tipo de assento, linha e coluna devem ser especificados para Executivo")

            if tipo_assento.lower() == "semi-leito":
                matriz = onibus.get_assentos_semi_leito()
            elif tipo_assento.lower() == "leito":
                matriz = onibus.get_assentos_leito()
            else:
                return (False, "Tipo de assento inválido para Executivo")

            if linha < 0 or linha >= len(matriz) or coluna < 0 or coluna >= len(matriz[linha]):
                return (False, "Linha ou coluna inválida para o assento escolhido")

            assento_obj = matriz[linha][coluna]
            if assento_obj.get_ocupado():
                return (False, "Assento já ocupado")

            assento_obj.set_passageiro(passageiro)
            assento_obj.set_ocupado(True)
            sucesso = True
            assento_str = assento_obj.get_numero()

        if not sucesso:
            return (False, "Falha ao reservar o assento")

        preco_final = viagem.get_preco()
        if isinstance(onibus, OnibusExecutivo) and tipo_assento and tipo_assento.lower() == "leito":
            preco_final *= 1.5
        if passageiro.eh_isento_de_pagamento():
            preco_final = 0.0

        passagem = Passagem(viagem, passageiro, assento_str)
        # ajustar o preço diretamente (se quiser eu testo e removo depois e crio um setter)
        passagem._Passagem__preco = preco_final
        self.__passagens.append(passagem)
        return (True, passagem)

    def buscar_passagem_por_bilhete(self, bilhete_numero):
        for p in self.__passagens:
            if p.get_bilhete() == bilhete_numero:
                return p
        return None

    def liberar_assento_da_passagem(self, passagem):
        viagem_atual = passagem.get_viagem()
        onibus = viagem_atual.get_onibus()
        numero_assento = passagem.get_assento()
        if not numero_assento:
            return False

        # Tenta liberar em Convencional (se existir)
        try:
            if hasattr(onibus, 'get_assentos'):
                for a in onibus.get_assentos():
                    if a.get_numero() == numero_assento:
                        a.set_passageiro(None)
                        a.set_ocupado(False)
                        return True
        except Exception:
            pass

        # Tenta liberar em Executivo com helper
        if isinstance(onibus, OnibusExecutivo):
            return onibus.libera_assento_por_numero(numero_assento)

        return False

    def trocar_passagem(self, bilhete_numero, nova_viagem, tipo_assento=None, linha=None, coluna=None, novo_assento_str=None):
        passagem_atual = self.buscar_passagem_por_bilhete(bilhete_numero)
        if passagem_atual is None:
            return (False, "Bilhete não encontrado")

        # prepara dados do passageiro para tentar reservar na nova viagem
        p = passagem_atual.get_passageiro()
        dados_passageiro = {
            'nome': p.get_nome(),
            'idade': p.get_idade(),
            'cpf': p.get_cpf(),
            'email': p.get_email(),
            'telefone': p.get_telefone(),
            'pcd': p.get_eh_PCD()
        }

        # Tenta reservar novo assento na nova viagem (sem liberar o antigo ainda)
        if isinstance(nova_viagem.get_onibus(), OnibusConvencional):
            if not novo_assento_str:
                return (False, "Para Convencional informe número do assento")
            dados_passageiro['assento'] = novo_assento_str
            success, resultado = self.vender_passagem(nova_viagem, dados_passageiro)
        else:
            success, resultado = self.vender_passagem(nova_viagem, dados_passageiro, tipo_assento, linha, coluna)

        if not success:
            return (False, f"Não foi possível reservar o novo assento: {resultado}")

        # nova passagem criada (resultado)
        nova_passagem = resultado

        # Agora que a nova reserva foi feita com sucesso, liberar o antigo
        self.liberar_assento_da_passagem(passagem_atual)

        # Atualizar passagem_atual para apontar para nova viagem/assento (mantendo o mesmo bilhete)
        passagem_atual.set_viagem(nova_passagem.get_viagem())
        passagem_atual.set_assento(nova_passagem.get_assento())
        passagem_atual._Passagem__preco = nova_passagem.get_preco()

        # remover a passagem temporária criada (vamos manter apenas a passagem_atual com o mesmo bilhete)
        try:
            self.__passagens.remove(nova_passagem)
        except ValueError:
            pass

        return (True, passagem_atual)
