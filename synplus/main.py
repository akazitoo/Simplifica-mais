from utils import functions

"""
```bash 
❯ python3 main.py

   Copyright (c), Simplifica+ 2021
   Email comments or suggestions to <contato@simplifica.mais>

   Synplus v0.01.pre (built-with python)
   Programa interno desenvolvido pelos membros de computação da Simplifica+


?. Login: admin
?. Senha: admin
 
# Outra conta registrada
?. Login: data
?. Senha: viewer
```
"""

functions.synplus_init()

print("   Copyright (c), Simplifica+ 2021")
print("   Email comments or suggestions to <contato@simplifica.mais>")  # It's a fake mail

print('\n   Synplus v0.01.pre (built-with python)')
print('   Programa interno desenvolvido pelos membros de computação da Simplifica+ \n\n')

user = input('?. Login: ')
password = input('?. Senha: ')

user_level = functions.who(user, password)

if user_level == "guest":
    print('\n~. Conta não registrada.')
    
is_to_repeat = True
exit = False

while is_to_repeat:

    while user_level == "admin" and not exit:
        print("\n>. [1] Inserir dados da tabela DATA.")
        print(">. [2] Atualizar dados da tabela DATA.")
        print(">. [3] Ler dados da tabela DATA.")
        print(">. [4] Remover dados da tabela DATA.") 
        print(">. [0] Sair.")

        option = input('\n?. Escolha [01234]: ')

        if option == '1':
            confirmation = input("\n.: Deseja inserir dados (S/N)? ")
            
            if confirmation.lower() == 's':
                city = input("\n?. Informe o município do(a) usuário(a): ")
                gender = input("?. Informe o gênero do(a) usuário(a): ")
                lgbtqia_plus  = input("?. Informe a sigla LGBTQIA+: ")

                city = city.lower().replace("ã", "a").replace(" ", "")
                gender = gender.lower().replace("á", "a")
                lgbtqia_plus = lgbtqia_plus.lower()

                functions.insert_data(city, gender, lgbtqia_plus)
            elif confirmation.lower() == 'n':
                pass
            else:
                print('\n&. Escolha Inválida')

        elif option == '2':
            confirmation = input("\n.: Deseja atualizar dados (S/N)? ")
            
            if confirmation.lower() == 's':
                user_id = input("\n?. Informe o id do(a) usuário(a): ")
                city = input("?. Informe o município do(a) usuário(a): ")
                gender = input("?. Informe o gênero do(a) usuário(a): ")
                lgbtqia_plus = input("?. Informe a sigla LGBTQIA+: ")

                city = city.lower().replace("ã", "a").replace(" ", "")
                gender = gender.lower().replace("á", "a")
                lgbtqia_plus = lgbtqia_plus.lower()

                functions.update_data(user_id, city, gender, lgbtqia_plus)
                
            elif confirmation.lower() == 'n':
                pass
            else:
                print('\n&. Escolha Inválida')

        elif option == '3':
            confirmation = input("\n.: Deseja ler dados (S/N)? ")
            
            if confirmation.lower() == 's':
                city = input("\n?. Informe o município para leitura: ")
                city = city.lower().replace("ã", "a").replace(" ", "")

                functions.read_data(city)

            elif confirmation.lower() == 'n':
                pass
            else:
                print('\n&. Escolha Inválida')

        elif option == '4':
            confirmation = input("\n.: Deseja remover dados (S/N)? ")
            
            if confirmation.lower() == 's':
                user_id = input("\n?. Informe o id do(a) usuário(a): ")

                functions.remove_data(id)

            elif confirmation.lower() == 'n':
                pass
            else:
                print('\n&. Escolha Inválida')

        elif option == '0':        
            exit = True
        else:
            print('\n&. Escolha Inválida')
                
    while user_level == "viewer" and not exit:
        print('\n>. [1] Visualizar dados do acesso ao site.')
        print('>. [0] Sair.')

        option = input('\n?. Escolha [01]: ')

        if option == '1':
            functions.data_view()
        elif option == '0':
            exit = True
        else:
            print('\n&. Escolha Inválida')
        
    exit = True

    if exit: 
        run_again = input("\n.: Deseja executar novamente o programa (S/N)? ")

        if run_again.lower() == 's':
            user = input('\n?. Login: ')
            password = input('?. Senha: ')

            user_level = functions.who(user, password)

            if user_level == "guest":
                print('\n~. Conta não registrada.')
            else:
                exit = False     
        elif run_again.lower() == 'n':
            print('\n\n   Synplus, desenvolvido por Simplifica+\n')
            is_to_repeat = False
        else:
            print('\n&. Escolha Inválida')
