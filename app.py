import streamlit as st
from conn import get_client
from cadastrarItem import inserir_item, cadastrarAux, cadastrarMovimentacao

# Conexão com Google Sheets
client = get_client()
planilha_completa = client.open_by_key("1PvxGvU0oxKXLEvFBZTq3e57r9JfrD0yDN0KaTEKnJQA")
aba1 = planilha_completa.get_worksheet(0)  # aba1
aba2 = planilha_completa.get_worksheet(1)  # aba2
aba3 = planilha_completa.get_worksheet(2)  # aba3
aba4 = planilha_completa.get_worksheet(3)  # aba4

# Interface Streamlit
st.sidebar.title("Menu")
pagina = st.sidebar.selectbox("Navegação", ["Cadastro de Item", "Cadastrar Auxiliar", "Movimentações"])

# Página Cadastro de Item
if pagina == "Cadastro de Item":
    st.title("Cadastro de Item")

    with st.form(key="form_cadastro_item"):
        nome = st.text_input("Nome do Item")
        tipo_medida = st.selectbox("Tipo de Medida", ["", "KG", "Litros", "Unidades"])
        botao_cadastrar = st.form_submit_button("Cadastrar")

    if botao_cadastrar:
        if nome and tipo_medida:
            inserir_item(aba4, nome, tipo_medida)
            st.success("Item cadastrado com sucesso!")
        else:
            st.warning("Por favor, preencha todos os campos corretamente.")

# Página Cadastro de Auxiliar
if pagina == "Cadastrar Auxiliar":
    st.title("Cadastro de Auxiliar")

    with st.form(key="form_cadastro_auxiliar"):
        nome_auxiliar = st.text_input("Nome do Auxiliar")
        botao_cadastrar_auxiliar = st.form_submit_button("Cadastrar")

    if botao_cadastrar_auxiliar:
        if nome_auxiliar:
            sucesso = cadastrarAux(aba3, nome_auxiliar)
            if sucesso:
                st.success("Auxiliar cadastrado com sucesso!")
            else:
                st.error("Esse Nome já está cadastrado.")
        else:
            st.warning("Por favor, preencha o nome do auxiliar.")

# Página Movimentações (Entrada/Saída)
if pagina == "Movimentações":
    st.title("Cadastrar Entrada ou Saída de Produto")

    with st.form(key="form_movimentacoes"):
        # Tipo de movimentação
        tipo_opcoes = ["", "Entrada", "Saída"]
        tipo_movimentacao = st.selectbox("Tipo de Movimentação", tipo_opcoes)

        # Item
        nomes_itens = [linha[0] for linha in aba4.get_all_values()[1:] if linha]
        nomes_itens = [""] + nomes_itens  # Adiciona opção vazia
        item_selecionado = st.selectbox("Escolha o Item", nomes_itens)

        # Responsável
        dados_responsaveis = [linha[1] for linha in aba3.get_all_values()[1:] if len(linha) > 1]
        dados_responsaveis = [""] + dados_responsaveis  # Adiciona opção vazia
        responsavel_selecionado = st.selectbox("Responsável", dados_responsaveis)

        # Quantidade e Observação
        quantidade = st.number_input("Quantidade", min_value=0.0, format="%.2f")
        observacao = st.text_input("Observação (opcional)")

        botao_cadastrar_movimentacao = st.form_submit_button("Cadastrar Movimentação")

    if botao_cadastrar_movimentacao:
        # Verificação dos campos obrigatórios
        if not tipo_movimentacao or not item_selecionado or not responsavel_selecionado:
            st.warning("Por favor, preencha todos os campos obrigatórios.")
        else:
            sucesso = cadastrarMovimentacao(
                planilha=aba2,  # Movimentações
                tipo=tipo_movimentacao,
                item=item_selecionado,
                quantidade=quantidade,
                responsavel=responsavel_selecionado,
                observacao=observacao
            )

            if sucesso:
                st.success(f"{tipo_movimentacao} de {quantidade} registrada para o item '{item_selecionado}' com responsável '{responsavel_selecionado}'.")
