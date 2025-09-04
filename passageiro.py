class Passageiro:
    #A ideia é pra eh_PCD ser booleano
    def __init__(self,nome,idade,cpf,email,telefone,eh_PCD):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__PCD = eh_PCD
        self.__email = email
        self.__telefone = telefone
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_eh_PCD(self):
        return self.__PCD

    def set_eh_PCD(self, eh_PCD):
        self.__PCD = eh_PCD
    
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__PCD = email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def eh_isento_de_pagamento(self):
        if self.__PCD == True or self.__idade < 6 or self.__idade > 60:
            return True
        else:
            return False
