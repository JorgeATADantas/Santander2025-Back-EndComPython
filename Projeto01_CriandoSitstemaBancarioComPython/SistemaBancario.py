
print("\n\nBem-vindo ao Sistema do Banco")

# Saldo inicial
saldo = 0

# Quantidade de saques realizados
quant_saques = 0

# Extrato sem lançamentos
extrato =""

# Limites de Saques diários
LIMITE_DIARIO = 3
LIMITE_SAQUE  = 500

while True:
    print(f"""          
          Escolha uma opção abaixo:
          
          [1] Depósito
          [2] Saque
          [3] Extrato
          [0] Sair
          """) 

    operacao = input('Digite a operação desejada:')

    if operacao == '1':
        print('-----------------------------------------------------')
        print('DEPÓSITO')
        print('-----------------------------------------------------')
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor <=0:
            print('Valor inválido, depósito não realizado')
        else:
            saldo +=valor
            extrato += (f"Depósito\t\t R$ {valor:>10.2f}\n")
            print("Depósito realizado com sucesso")

    elif operacao == '2':
        print('-----------------------------------------------------')
        print('SAQUE')
        print('-----------------------------------------------------')
        valor = float(input("Digite o valor que deseja sacar: "))

        if valor <=0:
            print('Valor inválido, saque não realizado')
            
        elif (valor > saldo):
            print('Saldo insuficiente')
            
        elif (valor > LIMITE_SAQUE):
            print(f'Limite de valor do saque excedido. O limite é {LIMITE_SAQUE}')
            
        else:
            quant_saques += 1

            if(quant_saques > LIMITE_DIARIO):
                print(f'A quantidade de saques diários foi excedida. O limite é {LIMITE_DIARIO}')
            else:
                saldo -= valor
                extrato += (f"Saque\t\t\t R$ {valor:>10.2f}\n")
                print("Saque realizado com sucesso")

    elif operacao == '3':
        print('-----------------------------------------------------')
        print('EXTRATO DE CONTA CORRENTE')
        print('-----------------------------------------------------')
        print(extrato)
        print(f'\nSaldo\t\t\t R$ {saldo:>10.2f}')
    
    elif operacao == '0':
        break

    else:
        print("Opção inválida")














