# sistema bancario com opcoes de deposito , saque e extrato

nome = input("Ola!, qual seu nome?\n =>")

print(f"Seja Bem Vindo {nome}!")

valor = 0
saldo = 0
limite = 500
opcao = -1
contador = 0

depositos = []
saques = []

num_deposito = 0
num_saques = 0



while opcao != 0:

    opcao = int(input("O que deseja fazer agora?\n [1] Depositar \n [2] Saque \n [3] Extrato \n [0] Sair \n =>"))

    if  opcao > 3 or opcao < 0:
        print("Insira um numero valido.\n")

    ## DEPOSITO

    if opcao == 1:
        valor_deposito = int(input("Insira o valor de deposito\n =>"))

        saldo += valor_deposito

        print(f"Seu saldo agora e : R${saldo}")
        print("")
        num_deposito += 1
        
        depositos.append(f"Deposito: {num_deposito}| Valor: R${valor_deposito}")
        

    ## SAQUE
    if opcao == 2:
        
        if saldo < 0:
            print("Nao e possivel realizar o saque, saldo indisponivel\n")

        elif contador >=3:
            print("Limite de Saque Diarios alcancado, tente novamente amanha.\n")    

        else:
            valor = int(input("Insira o valor que deseja sacar\n =>"))
            print("")

            if valor > saldo or valor > limite :
                print("Este valor nao pode ser sacado\n")
            else:
                num_saques += 1      
                saques.append(f"saque: {num_saques}|valor: R${valor}")

                contador +=1
                saldo -= valor
                print(f"Valor sacado com sucesso {nome.upper()}!")
                print(f"Seu saldo agora: R${saldo}")
                print("")
                
          
    if opcao == 3:
         print(f"Seus depositos: {depositos}\n")                       
         print(f"Seus saques: {saques}\n")                       
         print(f"Seu saldo agora: R${saldo}")                      
     
    if opcao == 0:
         break                      


