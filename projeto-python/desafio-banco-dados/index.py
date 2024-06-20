menu = """

Depositar [3]
Sacar [2]
Extrato [1]
Salir [0]

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
Limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "3":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
             saldo += valor 
             extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
       
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
          valor = float(input("informe o valor do saque: "))

          excedeu_saldo = valor > saldo

          excedeu_limite = valor > limite

          excedeu_saque = numero_saques >= Limite_saques

          if excedeu_saldo:
            print("Operação falhou! não tem saldo suficiente. ")

          elif excedeu_limite:
              print("Operação falhou! o valor do saque excedeu o limite. ")

          elif excedeu_saque:
              print("Operação falhou! Numero maximo de saque excedeu. ")

          elif valor > 0:
              saldo -= valor 
              extrato += f"saque: R$ {valor:.2f}\n"
              numero_saques += 1

          else:
            print("Operação falhou! o valor informado é inválido.")

    elif opcao == "1":
        print("\n****************Extrato****************")
        print("Não foram realizadas movimentação," if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("########################################")
          
    elif opcao == "0":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operaççao desejada. ")
              