print('\n   Copyright (c), Simplifica+ 2021')
print('   Email comments or suggestions to <contato@simplifica.mais>')

print('\n   Synplus v0.01.pre (built-with python)')
print('   Programa interno desenvolvido pelos membros de computação da Simplifica+ \n\n')

user = input('?. Login: ')
password = input('?. Senha: ')

registered_accounts = {
    "Accounts": [
        ('admin', 'admin'), 
        ('data', 'view'),
        ('simplifica', 'mais')
    ]
}  # {ID: 001} em Componentes no DOCUMENTATION.md

authenticator = None  # {ID: 002} em Componentes no DOCUMENTATION.md

if user == registered_accounts["Accounts"][0][0]:
    if password == registered_accounts["Accounts"][0][1]:
        authenticator = 1

elif user == registered_accounts["Accounts"][1][0]:
    if password == registered_accounts["Accounts"][1][1]:
        authenticator = 2

elif user == registered_accounts["Accounts"][2][0]:
    if password == registered_accounts["Accounts"][2][1]:
        authenticator = 3

else:
    print('~. Conta não registrada.')
    authenticator = 0

is_to_repeat = True

while is_to_repeat:

    while authenticator == 1:
        print('\n>. [1] Registrar usuário para ambulatório LGTBQIA+.')  # {ID: 001} em Detalhamento no DOCUMENTATION.md
        print('>. [2] Registrar busca por atendimento imediato.')  # {ID: 002} em Detalhamento no DOCUMENTATION.md
        print('>. [3] Registrar metadados do Website.')  # {ID: 003} em Detalhamento no DOCUMENTATION.md
        print('>. [0] Sair.')

        option = input('\n?. Escolha [0123]: ')

        if option == '1':
            confirmation_question = input("\n.: Deseja registrar um usuário para ambulatório (S/N)? ")
            
            if confirmation_question.upper() == 'S':
                user_email = str(input("\n?. Informe o email do(a) usuário(a): "))
                user_locale = str(input("?. Informe a localidade do(a) usuário(a): "))
                outpatient  = str(input("?. Informe o ambulatório de encaminhamento: "))

                arquivo = open("db.txt", "a")

                arquivo.write("{0};  {1};  {2}\n".format(user_email, user_locale, outpatient))

                arquivo.close()
            elif confirmation_question.upper() == 'N':
                pass
            else:
                print('\n&. Escolha Inválida')

        elif option == '2':
            confirmation_question = input("\n.: Deseja registrar busca por atendimento imediato (S/N)? ")
            
            if confirmation_question.upper() == 'S':
                print("\n    ESCOLHA AINDA EM DESENVOLVIMENTO :') ")
            elif confirmation_question.upper() == 'N':
                pass
            else:
                print('\n&. Escolha Inválida')

        elif option == '3':
            confirmation_question = input("\n.: Deseja registrar metadados do Website (S/N)? ")
            
            if confirmation_question.upper() == 'S':
                print("\n    ESCOLHA AINDA EM DESENVOLVIMENTO :') ")
            elif confirmation_question.upper() == 'N':
                pass
            else:
                print('\n&. Escolha Inválida')

        elif option == '0':        
            authenticator = 0

        else:
            print('\n&. Escolha Inválida')
                
    while authenticator == 2:
        print('\n>. [1] Visualizar dados de acesso ao site.')  # {ID: 004} em Detalhamento no DOCUMENTATION.md
        print('>. [2] Visualizar dados por ambulatórios LGTBQIA+.')  # {ID: 005} em Detalhamento no DOCUMENTATION.md
        print('>. [3] Visualizar dados da busca por atendimento imediato.')  # {ID: 006} em Detalhamento no DOCUMENTATION.md
        print('>. [0] Sair.')

        option = input('\n?. Escolha [0123]: ')

        if option == '1':
            print("\n    ESCOLHA AINDA EM DESENVOLVIMENTO :') ")
            
        elif option == '2':
            print("\n    ESCOLHA AINDA EM DESENVOLVIMENTO :') ")
            
        elif option == '3':
            print("\n    ESCOLHA AINDA EM DESENVOLVIMENTO :') ")
            
        elif option == '0':
            authenticator = 0 
        
        else:
            print('\n&. Escolha Inválida') 

    while authenticator == 3:
        print('''
   Essa parte é referente aos fluxos lógicos que estão sendo desenvolvidos
   para serem utilizados em formulários no website do projeto.
        ''')

        first_question = input('.: Pergunta 1? ').upper()
        second_question = input('.: Pergunta 2? ').upper()
        third_question = input('.: Pergunta 3? ').upper()
        fourth_question = input('.: Pergunta 4? ').upper()
        
        final_question = input('.: Você tem interesse em marcar uma consulta em um dos ambulatórios LGTB+ da Região Metropolina do Recife (S/N)? ').upper()

        locale_test = 'jaboatão'.replace('ã', 'a')  # Isso é um teste, será removido.
        
        if locale_test.upper() == 'RECIFE':
            print('\n~. Policlínica Lessa de Andrade')
            print('~. Endereço: Estr. dos Remédios, 2416 - Madalena, Recife - PE, 50770-120')
            print('~. Telefone: (81) 3355-7805 \n')

            print('\n~. Hospital da Mulher do Recife')
            print('~. Endereço: Rod BR-101 s/n - Curado, Recife - PE, 50790-640')
            print('~. Telefone: (81) 2011-0100')
            # Dados podem estar errados 

        elif locale_test.upper() == 'CAMARAGIBE':
            print('\n~. Ambulatório LGBT Darlen Gasparelle')
            print('~. Endereço: R. Pedro de Paula Rocha - Centro, Camaragibe - PE, 54762-745')
            print('~. Telefone: (81) 3458-0694')

        elif locale_test.upper() == 'JABOATAO': 
            print('\n~. Ambulatório LGBT Darlen Gasparelle')
            print('~. Endereço: R. Pedro de Paula Rocha - Centro, Camaragibe - PE, 54762-745')
            print('~. Telefone: (81) 3458-0694')

        else:
            print('\n/. Infelizmente não possui um ambulatório na sua região')
            # Aqui pode explicar o que a pessoa deveria fazer já que não tem nenhum ambulatorio perto
            # Ou também explicar o por que a pessoa não pode ir pra esses.

        print('''
   AINDA EM DESENVOLVIMENTO
   BY: MEMBROS DE COMPUTAÇÃO, SIMPLIFICA+ 2021''')
        authenticator = 0

    if authenticator == 0: 
        run_again = input("\n.: Deseja executar novamente o programa (S/N)? ")

        if run_again.upper() == 'S':
            user = input('\n?. Login: ')
            password = input('?. Senha: ')

            if user == registered_accounts["Accounts"][0][0]:
                if password == registered_accounts["Accounts"][0][1]:
                    authenticator = 1
                    is_to_repeat = True

            elif user == registered_accounts["Accounts"][1][0]:
                if password == registered_accounts["Accounts"][1][1]:
                    authenticator = 2
                    is_to_repeat = True

            elif user == registered_accounts["Accounts"][2][0]:
                if password == registered_accounts["Accounts"][2][1]:
                    authenticator = 3
                    is_to_repeat = True

            else:
                print('~. Conta não registrada.')
                
        else:
            print('\n\n   Synplus, desenvolvido por Simplifica+\n')
            is_to_repeat = False
