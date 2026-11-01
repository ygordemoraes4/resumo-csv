# AGENTS.md

## O que é este projeto

resumo-csv: app local (Streamlit) que lê a planilha de chamadas exportada do CAD
do Corpo de Bombeiros e mostra o consolidado. Uso diário, por uma pessoa.

## Regra de negócio

- Entrada: CSV do CAD, separador `;`, codificação Windows-1252 (não é UTF-8).
- Todas as linhas contam como chamada atendida. Nenhuma é excluída.
- A categoria é a primeira letra da coluna `Natureza`
  (exemplo: `P02004 - VISTORIA ...` conta como `P`).
- Saída: uma linha `Total: N`, seguida de uma linha `LETRA - N` por categoria.
  Sem significado das letras.
- As categorias aparecem em ordem alfabética.

## Verificação

- `ruff check .` para estilo.
- `pytest -q` para testes.
- Não afirme que passou sem mostrar a saída real do comando.

## Dados sensíveis

- Planilhas reais do CAD trazem endereço e coordenadas de ocorrências.
- Nunca leia, copie, commite nem coloque dado real em teste, log ou mensagem de commit.
- Planilhas reais ficam em `data/bruto/`, fora do Git.
- Testes usam só arquivos fictícios em `tests/fixtures/`.

## Convenções

- A lógica de contagem não depende do Streamlit. A página só chama a lógica.
- Nomes de domínio em português; nomes técnicos em inglês.

## Fronteiras

- Não adicionar dependência nova sem perguntar.