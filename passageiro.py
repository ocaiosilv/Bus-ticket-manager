class Passageiro:
    def __init__(self, nome, idade, cpf, email, telefone, eh_PCD):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__PCD = eh_PCD

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_eh_PCD(self):
        return self.__PCD

    def set_eh_PCD(self, valor):
        self.__PCD = valor

    def eh_isento_de_pagamento(self):
        return self.__PCD or self.__idade < 6 or self.__idade > 60

    def __str__(self):
        return f"{self.__nome} ({self.__idade} anos) - CPF: {self.__cpf}"
