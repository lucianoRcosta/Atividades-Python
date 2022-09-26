import validarCNPJ as v

while True:
    print()
    cnpj_completo = input('Insira um cnpj nesse formato "xx.xxx.xxx/xxxx-xx": ')
    cnpj = v.formatarCNPJ(cnpj_completo)
    numero = v.checagemInput(cnpj_completo)

    if numero is None and cnpj is None:
        print('Insira o cnpj no formato correto!')
    else:
        break

cnpj = v.digito1(cnpj)
cnpj = v.digito2(cnpj)
cnpj_refatorado = v.refazerCPNJ(cnpj)
validar = v.validar(cnpj_completo, cnpj_refatorado)

print(f'cpnj original: {cnpj_completo}')
print(f'cpnj refeito: {cnpj_refatorado}') 
print(validar)