from datetime import datetime

# sistema bancario com opcoes de deposito , saque e extrato

# limite de 500$ por saque e 10 saques por dia


# funcoes


def verifica_usuario(nome, Usuario):
    digito = int(
        input(
            "Se voce ja possuir uma conta digite [0], ou digite 1 para criar uma conta:  "
        )
    )
    if digito < 1:
        print(f"Seja Bem Vindo {nome}!")
        return nome, Usuario
    else:
        print(f"Certo vou precisar somente do seu CPF, {nome}")
        print("")
        cpf = int(input("Digite seu CPF [11 digitos]"))

        # Verificar se o CPF já existe na lista de usuários
        for usuario in Usuario:
            if f"CPF:{cpf}" in usuario:  # Verifica se o CPF já está no registro
                print("CPF já cadastrado. Tente novamente.")
                return nome, Usuario
        Usuario.append(f"Nome: {nome} | CPF:{cpf}")

        print("Muito bem! Usuario cadastrado.")
        print("Agora voce ja pode fazer as suas operacoes")
        print(f"Seja Bem Vindo {nome}!")
        print(f"Usuario: {Usuario}")

        return nome, Usuario


def deposito(saldo, extrato):
    num_deposito = 0
    # Solicita ao usuário o valor do depósito
    valor = int(input("Insira o valor de depósito: R$"))

    # Atualiza o saldo
    saldo += valor

    num_deposito += 1

    # Adiciona o depósito ao extrato
    extrato.append(f"Depósito: {num_deposito} | Valor R${valor}")

    # Exibe o novo saldo
    print(f"Seu saldo agora é: R${saldo}")
    print("")

    return saldo, extrato


def saque(
    *,
    saldo,
    valor,
    extrato,
    limite,
    num_saques,
    data,
    data_saques,
    data_hora,
    data_hora_saques,
    saques,
    nome,
):

    if saldo <= 0:
        print("Não é possível realizar o saque, saldo indisponível\n")
    else:
        valor = int(input("Insira o valor que deseja sacar\n =>"))
        print("")

        if valor > saldo or valor > limite:
            print("Este valor não pode ser sacado\n")
        else:
            # Contar quantos saques foram realizados na data atual
            count = data_saques.count(data)

            # Verificar se o limite de 10 saques foi atingido
            if count > 9:
                print(
                    "Você atingiu o limite de saques para hoje, tente novamente amanhã.\n"
                )
            else:
                # Registrar o saque
                num_saques += 1
                saques.append(
                    f"Saque: {num_saques}| Valor: R${valor} | Data/Hora: {data_hora}"
                )
                saldo -= valor
                data_saques.append(data)  # Adiciona a data do saque à lista
                data_hora_saques.append(data_hora)

                print(f"Valor sacado com sucesso {nome.upper()}!")
                print(f"Seu saldo agora: R${saldo}")
                print("")

    return saldo, extrato


def criar_extrato(saques, saldo, extrato):
    print(f"Seus depositos: {extrato}\n")
    print(f"Seus saques: {saques}\n")
    print(f"Seu saldo agora: R${saldo}")
    return saques, saldo, extrato

    # Função principal para simular o fluxo


def main():

    # variaves
    valor = 0
    saldo = 0
    limite = 500
    opcao = -1

    Usuario = []
    saques = []
    extrato = []
    data_saques = []
    data_hora_saques = []

    num_saques = 0

    mascara_data = "%d/%m/%Y"
    mascara_data_hora = "%d/%m/%Y %H:%M"

    # Data atual no formato desejado
    data_atual = datetime.now()
    data = data_atual.strftime(mascara_data)

    data_hora = data_atual.strftime(mascara_data_hora)

    # Inicio

    nome = input("Ola!, qual seu nome?\n =>")

    nome, Usuario = verifica_usuario(nome, Usuario)

    while opcao != 0:
        opcao = int(
            input(
                "O que deseja fazer agora?\n [1] Depositar \n [2] Saque \n [3] Extrato \n [0] Sair \n =>"
            )
        )

        if opcao > 3 or opcao < 0:
            print("Insira um numero valido.\n")

        ## DEPOSITO
        if opcao == 1:

            # Chama a função deposito
            saldo, extrato = deposito(saldo, extrato)
        ## SAQUE
        if opcao == 2:

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                data=data,
                data_saques=data_saques,
                data_hora=data_hora,
                data_hora_saques=data_hora_saques,
                saques=saques,
                nome=nome,
            )
        ## EXTRATO
        if opcao == 3:
            saques, saldo, extrato = criar_extrato(saques, saldo, extrato)

        ## SAIR
        if opcao == 0:
            print("Obrigado por usar nosso serviço!")
            break


main()
