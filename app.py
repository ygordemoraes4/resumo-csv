import streamlit as st

from resumo.contagem import COLUNA_NATUREZA, contar_chamadas, formatar_resumo

st.title("Resumo de chamadas")

arquivo = st.file_uploader("Planilha do CAD (.csv)", type="csv")

if st.button("OK", disabled=arquivo is None):
    try:
        total, categorias = contar_chamadas(arquivo.getvalue())
    except KeyError:
        st.error(f"Coluna {COLUNA_NATUREZA} não encontrada.")
    else:
        st.code(formatar_resumo(total, categorias), language=None)
