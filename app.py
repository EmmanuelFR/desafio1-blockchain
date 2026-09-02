"""Interface da blockchain educacional construída com Streamlit."""

import streamlit as st

from blockchain import Blockchain


st.set_page_config(
    page_title="Blockchain Educacional",
    page_icon="⛓️",
    layout="wide",
)

if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()

blockchain: Blockchain = st.session_state.blockchain

st.title("Blockchain Educacional")
st.caption("Simulação acadêmica de uma cadeia de blocos")

st.info(
    "Esta aplicação demonstra a criação e o encadeamento de blocos por meio "
    "de hashes SHA-256, além da verificação da integridade dos registros."
)

rotulos_carteiras = {
    identificador: f"{carteira['usuario']} ({identificador})"
    for identificador, carteira in blockchain.carteiras.items()
}
identificadores_carteiras = list(rotulos_carteiras)

st.subheader("Nova transação")
st.caption("Cada transação válida atualiza os saldos e gera um novo bloco.")

with st.form("formulario_transacao"):
    origem = st.selectbox(
        "Carteira de origem",
        identificadores_carteiras,
        format_func=rotulos_carteiras.get,
    )
    destino = st.selectbox(
        "Carteira de destino",
        identificadores_carteiras,
        index=1,
        format_func=rotulos_carteiras.get,
    )
    valor = st.number_input(
        f"Valor ({blockchain.moeda})",
        min_value=1,
        value=1,
        step=1,
    )
    enviar_transacao = st.form_submit_button(
        "Realizar transação",
        type="primary",
    )

if enviar_transacao:
    transacao_realizada, mensagem_transacao = blockchain.realizar_transacao(
        origem,
        destino,
        valor,
    )
    if transacao_realizada:
        st.success(mensagem_transacao)
    else:
        st.error(mensagem_transacao)

st.subheader("Demonstração de adulteração")
st.caption(
    "Altere intencionalmente o valor registrado em um bloco para verificar "
    "se a cadeia identifica a inconsistência."
)

blocos_transacao = [
    bloco
    for bloco in blockchain.cadeia
    if bloco.dados.get("tipo") == "transacao"
]

if blocos_transacao:
    indices_blocos = [bloco.indice for bloco in blocos_transacao]

    with st.form("formulario_adulteracao"):
        indice_adulterado = st.selectbox(
            "Bloco que será adulterado",
            indices_blocos,
            format_func=lambda indice: f"Bloco {indice}",
        )
        novo_valor_adulterado = st.number_input(
            f"Novo valor registrado ({blockchain.moeda})",
            min_value=1,
            value=999,
            step=1,
        )
        enviar_adulteracao = st.form_submit_button(
            "Simular adulteração",
        )

    if enviar_adulteracao:
        adulteracao_realizada, mensagem_adulteracao = (
            blockchain.simular_adulteracao(
                indice_adulterado,
                novo_valor_adulterado,
            )
        )
        if adulteracao_realizada:
            st.warning(mensagem_adulteracao)
        else:
            st.error(mensagem_adulteracao)
else:
    st.info(
        "Realize uma transação para criar um bloco que possa ser adulterado."
    )

if st.button(
    "Reiniciar demonstração",
    help=(
        "Descarta os blocos e saldos atuais desta sessão e restaura "
        "o estado inicial."
    ),
):
    st.session_state.blockchain = Blockchain()
    st.rerun()

cadeia_valida, mensagem_validacao = blockchain.validar_cadeia()

coluna_blocos, coluna_status = st.columns(2)
with coluna_blocos:
    st.metric("Quantidade de blocos", len(blockchain.cadeia))
with coluna_status:
    st.metric("Integridade da cadeia", "Válida" if cadeia_valida else "Inválida")

if cadeia_valida:
    st.success(mensagem_validacao)
else:
    st.error(mensagem_validacao)

st.subheader("Carteiras educacionais")

colunas_carteiras = st.columns(len(blockchain.carteiras))
for coluna, (identificador, carteira) in zip(
    colunas_carteiras,
    blockchain.carteiras.items(),
):
    with coluna:
        st.markdown(f"**{carteira['usuario']}**")
        st.caption(identificador)
        st.metric(
            "Saldo disponível",
            f"{carteira['saldo']} {blockchain.moeda}",
        )

st.subheader("Blocos registrados")

for bloco in blockchain.cadeia:
    with st.expander(f"Bloco {bloco.indice}", expanded=True):
        st.write(f"**Data e hora (UTC):** {bloco.data_hora}")
        st.write("**Hash anterior:**")
        st.code(bloco.hash_anterior, language=None)
        st.write("**Hash do bloco:**")
        st.code(bloco.hash, language=None)
        st.write("**Dados armazenados:**")
        st.json(bloco.dados)
