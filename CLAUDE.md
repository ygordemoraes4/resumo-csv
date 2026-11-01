@AGENTS.md

# Instruções específicas do Claude Code

## Fluxo de trabalho esperado

1. Antes de editar mais de um arquivo, apresente o plano e espere minha aprovação.
2. Implemente.
3. Rode `ruff check .` e `pytest -q`. Mostre a saída real; não afirme que passou.
4. Só depois proponha o commit.

## Quando perguntar em vez de decidir

- A tarefa muda a regra de contagem.
- A tarefa exige uma dependência nova.
- Uma instrução conflita com o AGENTS.md. Aponte o conflito.

## Commits

- Mensagem em inglês, no imperativo, primeira linha até 72 caracteres.
- Prefixos: `feat:`, `fix:`, `docs:`, `test:`, `chore:`.
- Nunca faça `git push` sem pedido explícito.
- Nunca inclua dado real de ocorrência na mensagem.