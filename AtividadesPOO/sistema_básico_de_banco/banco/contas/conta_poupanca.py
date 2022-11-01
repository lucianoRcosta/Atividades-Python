from banco.contas.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self , agencia = 'std', nmr_conta = 0, saldo = 0, tipo_de_conta = 0):
        super().__init__(agencia, nmr_conta, saldo)
        self.__tipo_de_conta = tipo_de_conta
    
    @property
    def tipo_de_conta(self):
        return self.__tipo_de_conta

    @tipo_de_conta.setter
    def tipo_de_conta(self, valor):
        self.__tipo_de_conta = 0

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor de saque tem que ser numérico !')
        
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            raise ValueError('Valor de saque não pode ser superior ao saldo !')    
    