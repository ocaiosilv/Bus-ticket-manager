# onibus_executivo.py
from onibus import Onibus
from assento import Assento


# Mudei issaqui tudo, inclusive dps tire os comentários, aqui tava daquele jeito antigo, ai eu fiz do teu jeito la
# so que mudei a sigla ne pros assentos, ai ficou tipo ah S - A1, semileito a1, L - A1, leito a1,e é isso
# a logica é a merma de convencional la, so que ai nao tava funcionando na troca, ai pedi pro gepeto ajeitar, ai ele fez umas funçãod e localizar o assento ai
# mas isso precisa mudar nao, acho que ta funcionando suave, so nao gostei do imprime, mude ai na moral, ta feio p peste

class OnibusExecutivo(Onibus):
    def __init__(self, modelo, fabricante, numrodas, descricao):
        super().__init__(modelo, fabricante, numrodas, descricao, "Executivo")
        self.__assentos_semi_leito = self.gera_assentos_semi_leito()
        self.__assentos_leito = self.gera_assentos_leito()

    def gera_assentos_semi_leito(self):
        fileiras = "ABCDEFGHIJKL"
        matriz = []
        for numero in range(1, 5):  # 1..4
            linha = []
            for letra in fileiras:
                numero_do_assento = f"S - {letra}{numero}"
                linha.append(Assento(numero_do_assento, False))
            matriz.append(linha)
        return matriz

    def gera_assentos_leito(self):
        fileiras = "ABCD"
        matriz = []
        for numero in range(1, 4):  # 1..3
            linha = []
            for letra in fileiras:
                numero_do_assento = f"L - {letra}{numero}"
                linha.append(Assento(numero_do_assento, False))
            matriz.append(linha)
        return matriz

    def get_assentos_semi_leito(self):
        return self.__assentos_semi_leito

    def get_assentos_leito(self):
        return self.__assentos_leito

    def localiza_assento(self, numero_assento_procurado):
        # procura em semi
        for i, linha in enumerate(self.__assentos_semi_leito):
            for j, assento in enumerate(linha):
                if assento.get_numero() == numero_assento_procurado:
                    return assento, ("Semi-Leito", i, j)
        # procura em leito
        for i, linha in enumerate(self.__assentos_leito):
            for j, assento in enumerate(linha):
                if assento.get_numero() == numero_assento_procurado:
                    return assento, ("Leito", i, j)
        return None, (None, None, None)

    def set_assento_por_posicao(self, tipo_assento, linha_idx, coluna_idx, passageiro):
        if tipo_assento.lower() == "semi-leito":
            matriz = self.__assentos_semi_leito
        elif tipo_assento.lower() == "leito":
            matriz = self.__assentos_leito
        else:
            return False
        if linha_idx < 0 or linha_idx >= len(matriz) or coluna_idx < 0 or coluna_idx >= len(matriz[linha_idx]):
            return False
        assento = matriz[linha_idx][coluna_idx]
        if assento.get_ocupado():
            return False
        assento.set_passageiro(passageiro)
        assento.set_ocupado(True)
        return True

    def set_assento(self, numero_assento, passageiro):
        assento, _ = self.localiza_assento(numero_assento)
        if assento and not assento.get_ocupado():
            assento.set_passageiro(passageiro)
            assento.set_ocupado(True)
            return True
        return False

    def libera_assento_por_numero(self, numero_assento):
        assento, _ = self.localiza_assento(numero_assento)
        if assento:
            assento.set_passageiro(None)
            assento.set_ocupado(False)
            return True
        return False

    def imprime(self):
        super().imprime()
        livres_sl = sum(1 for l in self.__assentos_semi_leito for a in l if not a.get_ocupado())
        total_sl = sum(len(l) for l in self.__assentos_semi_leito)
        livres_l = sum(1 for l in self.__assentos_leito for a in l if not a.get_ocupado())
        total_l = sum(len(l) for l in self.__assentos_leito)
        print(f"Assentos Semi-Leito: {total_sl} (Livres: {livres_sl})")
        print(f"Assentos Leito: {total_l} (Livres: {livres_l})")
