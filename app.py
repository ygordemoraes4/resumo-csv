import streamlit as st

from summary.count import NATURE_COLUMN, count_calls, format_summary

st.title("Resumo de chamadas")

uploaded_file = st.file_uploader("Planilha do CAD (.csv)", type="csv")

if st.button("OK", disabled=uploaded_file is None):
    try:
        total, categories = count_calls(uploaded_file.getvalue())
    except KeyError:
        st.error(f"Coluna {NATURE_COLUMN} não encontrada.")
    else:
        st.code(format_summary(total, categories), language=None)
