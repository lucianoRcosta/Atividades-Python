from banco.contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia = 'std', nmr_conta = 0, saldo = 0, limite = 100, tipo_de_conta = 1):
        super().__init__(agencia, nmr_conta, saldo)
        self.__limite = limite
        self.__tipo_de_conta = tipo_de_conta

    @property
    def tipo_de_conta(self):
        return self.__tipo_de_conta

    @property
    def limite(self):
        return self.__limite 

    @limite.setter
    def limite(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do limite da conta corrente tem que ser numérico !')
        
        self.__limite = valor

    @tipo_de_conta.setter
    def tipo_de_conta(self, valor):
        self.__tipo_de_conta = 1

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor de saque tem que ser numérico !')
        
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
        else:
            raise ValueError('Valor de saque não pode ultrapassar o limite !') 
