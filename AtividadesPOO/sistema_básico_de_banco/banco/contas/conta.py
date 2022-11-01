"""
Aqui é onde fica a super classe Conta
"""
from abc import abstractclassmethod, ABC


class Conta(ABC):
    def __init__(self, agencia , nmr_conta , saldo):
        self.__agencia = agencia
        self.__nmr_conta = nmr_conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def nmr_conta(self):
        return self.__nmr_conta
    
    @property 
    def saldo(self):
        return self.__saldo

    @agencia.setter
    def agencia(self, valor):
        if not isinstance(valor, str):
            raise ValueError('Agencia precisa ser em string !')

        self.__agencia = valor
   
    @nmr_conta.setter
    def nmr_conta(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Número da conta precisa ser int !')

        self.__nmr_conta = valor

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do saldo tem que ser numérico !')

        self.__saldo = valor        
    
    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Depósito tem que ser numérico !')
        
        self.__saldo += valor
    
    @abstractclassmethod
    def sacar(self, valor):
        pass


            
