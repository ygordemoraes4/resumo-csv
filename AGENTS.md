# AGENTS.md

## O que é este projeto

resumo-csv: app que lê a planilha de chamadas exportada do CAD do Corpo de
Bombeiros e mostra o consolidado. Uso diário, por uma pessoa.

Duas páginas chamam a mesma lógica de `summary/`:

- `app.py`: página local em Streamlit (`run.bat`).
- `index.html`: página estática no GitHub Pages. Roda o Python no navegador com
  Pyodide (v314.0.7, via CDN jsDelivr); a planilha é processada no computador de
  quem usa.

## Regra de negócio

- Entrada: CSV do CAD, separador `;`, codificação Windows-1252 (não é UTF-8).
- Todas as linhas contam como chamada atendida. Nenhuma é excluída.
- A categoria é a primeira letra da coluna `Natureza`
  (exemplo: `P02004 - VISTORIA ...` conta como `P`).
- Saída: uma linha `Total: N`, seguida de uma linha `LETRA - N` por categoria.
  Sem significado das letras.
- As categorias aparecem em ordem alfabética.

## Regra de negócio: atendimentos por viatura

- Fonte: a mesma planilha do CAD, só na `index.html` (aba Viaturas).
- Viatura vem da coluna `Recursos empenhados`. Vários recursos na mesma chamada
  vêm separados por `/`; a chamada aparece uma vez para cada recurso.
- Chamada sem recurso é ignorada nesta saída (e continua contando no resumo).
- Colunas: hora saída (`Data/hora de criação`), hora chegada
  (`Data/hora da situação atual`), od. saída e od. chegada (vazios), endereço
  (`Local do fato`) e motorista (vazio). Data e hora aparecem juntas.
- Viaturas em ordem alfabética; atendimentos de cada viatura em ordem
  cronológica de saída.
- Od. saída, od. chegada e motorista são preenchidos na página, que oferece
  copiar, exportar CSV e imprimir. Nada disso sai do navegador.

## Verificação

- `ruff check .` para estilo.
- `pytest -q` para testes.
- Não afirme que passou sem mostrar a saída real do comando.

## Dados sensíveis

- Planilhas reais do CAD trazem endereço e coordenadas de ocorrências.
- Nunca leia, copie, commite nem coloque dado real em teste, log ou mensagem de commit.
- Planilhas reais ficam em `data/raw/`, fora do Git.
- Testes usam só arquivos fictícios em `tests/fixtures/`.
- Nenhuma página pode enviar a planilha, ou parte dela, a um servidor. A
  `index.html` só faz requisições para o Pyodide e para `summary/count.py`.

## Convenções

- A lógica de contagem não depende do Streamlit nem do navegador. As páginas só
  chamam a lógica; a regra existe só em `summary/`.
- Nomes no código (arquivos, funções, variáveis, testes) em inglês; interface e documentação em português.
- Exceção: os nomes das colunas do CSV do CAD (`Natureza`, `Recursos empenhados`,
  `Data/hora de criação` etc.) ficam como vêm na planilha.

## Fronteiras

- Não adicionar dependência nova sem perguntar.