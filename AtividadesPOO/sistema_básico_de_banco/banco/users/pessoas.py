"""
Aqui é onde fica a super classe Pessoa
"""

class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        # if not isinstance(valor, str):
        #     raise ValueError('Nome precisa ser Válido !')
        aux = valor.replace(' ', '')
        if not aux.isalpha():
            raise ValueError('Nome precisa ser Válido !')
            
        self.__nome = valor.title()
    
    @property
    def idade(self):
        return self.__idade
    
    
    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, (int)):
            raise ValueError('Idade precisa ser Válida !')
        
        if valor >= 18:
            self.__idade = valor
        else:
            raise ValueError('Menor de Idade !')


