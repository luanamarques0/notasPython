from connDB import create_user,create_note,exibir_notes

menssagem = """
       Bem-vindo ao NotasPython!
    -------------------------------
        Escolha uma das opções:
         1 - Criar noov úsuario:
         2 - Criar uma nova nota:
         3 - Exibir todas as notas:
         4 - Sair
    """
print(menssagem)

opcao = int(input("Qual sua escolha? "))

while opcao in (1,2,3,4):
    if opcao == 1:
        nome = input("Digite seu nome: ")
        create_user(nome)

        print(menssagem)
        opcao = int(input("Qual sua escolha? "))

    elif opcao == 2:
        nome = input("Digite seu nome: ")
        titulo = input("Digite um titulo para sua nota: ")
        note = input("Digite sua nota: ")
        create_note(nome,titulo,note)
        
        print(menssagem)
        opcao = int(input("Qual sua escolha? "))
    
    elif opcao == 3:
        nome = input("Digite seu nome: ")
        exibir_notes(nome)
        print(menssagem)
        opcao = int(input("Qual sua escolha? "))
    
    else:
        print("Agradecemos por usar nosso sistema, até a próxima!")
        break