import datetime

def inserir_item(planilha, nome, tipo_medida):
    data_cadastro = datetime.datetime.now().strftime("%d/%m/%Y")
    nova_linha = [nome, tipo_medida, data_cadastro]
    planilha.append_row(nova_linha)


def cadastrarAux(planilha, nome):
    # Pega todos os nomes já cadastrados
    nomes_existentes = [linha[0].strip().lower() for linha in planilha.get_all_values()[1:] if linha]

    # Verifica se o nome já existe (ignorando maiúsculas/minúsculas e espaços extras)
    if nome.strip().lower() in nomes_existentes:
        return False  # Já existe

    data_cadastro = datetime.datetime.now().strftime("%d/%m/%Y")
    nova_linha = [nome.strip(), data_cadastro]
    planilha.append_row(nova_linha)
    return True  # Cadastrado com sucesso

def cadastrarMovimentacao(planilha, tipo, item, quantidade, responsavel, observacao):
    # Buscar todas as linhas da planilha
    dados = planilha.get_all_values()
    
    # Se já existem dados além do cabeçalho
    if len(dados) > 1:
        ultimo_id = int(dados[-1][0])  # Pega o primeiro valor da última linha (coluna ID)
        novo_id = ultimo_id + 1
    else:
        novo_id = 1  # Se não houver dados (só cabeçalho), começa no 1

    data_cadastro = datetime.datetime.now().strftime("%d/%m/%Y")
    nova_linha = [novo_id, tipo, data_cadastro, item, quantidade, responsavel, observacao]
    
    planilha.append_row(nova_linha)
    return True