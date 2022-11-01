from banco.users.clientes import Cliente as cl
from banco.contas.conta_poupanca import ContaPoupanca as cp
from banco.contas.conta_corrente import ContaCorrente as cc
from banco.banco import Banco

# Há um problema nas classe, talvez o encapsulamento tenha de mudar ou atribuições tenham q ser feitas separadamente

banco = Banco()
c1 = cl()
c1.nome = 'luciano ramos'
c1.idade = 23

# c2 = cl()
# c2.nome = 'Luciano Ramos'

banco.autentificar_cliente(c1.nome)
# banco.autentificar_cliente(c2.nome)

cc1 = cc() # agencia, nmr_conta, saldo, limite
cc1.agencia = '2'
cc1.nmr_conta = 157
cc1.saldo = 250
cc1.limite = 300

banco.autentificador_agencia(cc1.agencia)
banco.autentificar_conta(cc1.nmr_conta)

cp1 = cp('BB', 157, 5000) # agencia, nmr_conta, saldo
cp1.saldo = 850
cp1.nmr_conta = 155
cp1.agencia = '1'

banco.autentificador_agencia(cp1.agencia)
banco.autentificar_conta(cp1.nmr_conta)

c1.add_conta(cc1)
c1.add_conta(cp1)
c1.mostrar_contas()

cp1.sacar(150)
cc1.deposito(500)

c1.mostrar_contas()
