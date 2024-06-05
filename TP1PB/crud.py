from datetime import datetime



compromissos = []

def verificar_data(data_str):
    """
    Verifica se a string de data fornecida está em um formato válido e retorna
    um objeto datetime se for válida.

    Parâmetros:
    data_str (str): A data no formato dd/mm/yyyy.

    Retorna:
    datetime: Objeto datetime se a data for válida.
    None: Se a data for inválida.
    """
    formato = "%d/%m/%Y"
    try:
        data_valida = datetime.strptime(data_str, formato)
        return data_valida
    except ValueError:
        return None

def incluir_compromisso():
    """
    Inclui um novo compromisso na lista de compromissos. Solicita ao usuário
    informações sobre o compromisso e verifica se a data do compromisso é válida
    e não está no passado.
    """
    nome = input("Digite o nome do compromisso: ")
    descricao = input("Digite a descrição do compromisso: ")
    data_hoje_criacao = datetime.now()
    
    while True:
        data_compromisso_str = input("Digite a data do compromisso (dd/mm/yyyy): ")
        data_compromisso = verificar_data(data_compromisso_str)
        if data_compromisso:
            if data_compromisso >= datetime.now():
                break
            else:
                print("Data inválida. Não é possível agendar compromissos no passado.")
        else:
            print("Data inválida. Tente novamente.")
    
    compromisso = {
        'id': len(compromissos) + 1,
        'nome': nome,
        'descricao': descricao,
        'data_criacao': data_hoje_criacao,
        'data_compromisso': data_compromisso,
        'concluido': False
    }
    compromissos.append(compromisso)
    print("Compromisso incluído com sucesso!")

def listar_compromissos():
    """
    Lista todos os compromissos armazenados, exibindo seus detalhes, incluindo
    ID, nome, descrição, data de criação, data do compromisso e status (Concluído ou Pendente).
    """
    if not compromissos:
        print("Nenhum compromisso agendado.")
    else:
        for compromisso in compromissos:
            status = "Concluído" if compromisso['concluido'] else "Pendente"
            print(f"ID: {compromisso['id']}")
            print(f"Nome: {compromisso['nome']}")
            print(f"Descrição: {compromisso['descricao']}")
            print(f"Data de criação: {compromisso['data_criacao'].strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Data do compromisso: {compromisso['data_compromisso'].strftime('%d/%m/%Y')}")
            print(f"Status: {status}")
            print("-" * 30)

def consultar_compromisso_id(compromisso_id):
    """
    Consulta um compromisso pelo seu ID.

    Parâmetros:
    compromisso_id (int): O ID do compromisso a ser consultado.

    Retorna:
    dict: O compromisso se encontrado.
    None: Se nenhum compromisso com o ID fornecido for encontrado.
    """
    for compromisso in compromissos:
        if compromisso['id'] == compromisso_id:
            return compromisso
    return None

def alterar_compromisso():
    """
    Altera os detalhes de um compromisso existente. Permite ao usuário alterar
    o nome, a descrição ou a data do compromisso.
    """
    try:
        compromisso_id = int(input("Entre com o número do ID do compromisso: "))
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return
    
    compromisso = consultar_compromisso_id(compromisso_id)
    
    if compromisso:
        print("O que você deseja alterar?")
        print("[1] - Nome")
        print("[2] - Descrição")
        print("[3] - Data do compromisso")
        
        try:
            oper = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Deve ser um número inteiro.")
            return
        
        if oper == 1:
            novo_nome = input("Entre com o novo nome: ")
            compromisso['nome'] = novo_nome
        elif oper == 2:
            nova_descricao = input("Entre com a nova descrição: ")
            compromisso['descricao'] = nova_descricao
        elif oper == 3:
            while True:
                nova_data_str = input("Entre com a nova data do compromisso (dd/mm/yyyy): ")
                nova_data = verificar_data(nova_data_str)
                if nova_data:
                    if nova_data >= datetime.now():
                        compromisso['data_compromisso'] = nova_data
                        break
                    else:
                        print("Data inválida. Não é possível agendar compromissos no passado.")
                else:
                    print("Data inválida. Tente novamente.")
        else:
            print("Operação inválida.")
        
        print("Compromisso alterado com sucesso!")
    else:
        print("Erro: Compromisso não existe.")

def excluir_compromisso():
    """
    Exclui um compromisso da lista de compromissos com base no seu ID.

    Parâmetros:
    compromisso_id (int): O ID do compromisso a ser excluído.
    """
    try:
        compromisso_id = int(input("Entre com o número do ID do compromisso: "))
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return
    
    compromisso = consultar_compromisso_id(compromisso_id)
    
    if compromisso:
        compromissos.remove(compromisso)
        print("Compromisso excluído com sucesso!")
    else:
        print("Erro: Compromisso não existe.")

def marcar_compromisso_concluido():
    """
    Marca um compromisso como concluído com base no seu ID.

    Parâmetros:
    compromisso_id (int): O ID do compromisso a ser marcado como concluído.
    """
    try:
        compromisso_id = int(input("Entre com o número do ID do compromisso: "))
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return

    compromisso = consultar_compromisso_id(compromisso_id)

    if compromisso:
        compromisso['concluido'] = True
        print("Compromisso marcado como concluído!")
    else:
        print("Erro: Compromisso não existe.")
