"""
Aqui é onde fica a classe cliente
"""
from banco.users.pessoas import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome = 'fulano', idade = '18'):
        super().__init__(nome, idade)
        self.__conta = []

    def add_conta(self ,conta):
        self.__conta.append(conta)
    
    def mostrar_contas(self):
        print(f'Cliente: {self.nome} ')
        print(f'Idade: {self.idade} ')
        print()
        for detalhes in self.__conta:
            print(f'Agência: {detalhes.agencia}')
            print(f'Número da Conta: {detalhes.nmr_conta}')
            print(f'Saldo: {detalhes.saldo}')
          
            if detalhes.tipo_de_conta == 1:
                print(f'Limite: {detalhes.limite}')
            print()