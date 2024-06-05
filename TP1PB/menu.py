from crud import *
def menu():
    while True:
        print("1. Incluir compromisso")
        print("2. Listar compromissos")
        print("3. Alterar compromisso")
        print("4. Excluir compromisso")
        print("5. Marcar compromisso como concluído")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            incluir_compromisso()
        elif opcao == '2':
            listar_compromissos()
        elif opcao == '3':
            alterar_compromisso()
        elif opcao == '4':
            excluir_compromisso()
        elif opcao == '5':
            marcar_compromisso_concluido()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")