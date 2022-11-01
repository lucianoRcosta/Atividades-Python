
class Banco():
    def __init__(self):
        self.__nome_clientes = []
        self.__nmr_contas = []
        self.__agencias = ['1', '2', '3', '4', '5']

    def autentificar_cliente(self, valor):
        for nome in self.__nome_clientes:
            if nome == valor:
                raise ValueError('Cliente já está presente no Banco !')
                
        self.__nome_clientes.append(valor)
        print('Cliente Autentificado !')

    def autentificar_conta(self, valor):
        for nmr in self.__nmr_contas:
            if nmr == valor:
                print('Conta já está presente no banco !')
                return

        self.__nmr_contas.append(valor)
        print('Conta Autentificada !')
    
    def autentificador_agencia(self, valor):
        aux = 0
        for agencia in self.__agencias:
            if agencia == valor:
                aux += 1
        
        if aux == 0:
            raise ValueError('Agência não consta no Banco !')
        
        print('Agência Autentificada !')