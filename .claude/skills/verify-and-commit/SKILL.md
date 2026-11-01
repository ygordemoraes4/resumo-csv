---
name: verify-and-commit
description: Roda o gate de verificação e prepara o commit no padrão do projeto. Use quando o usuário pedir para verificar, commitar ou fechar uma etapa.
disable-model-invocation: true
---

# Verificar e commitar

1. Rode `git status --short` e confira se só aparecem os arquivos esperados.
2. Rode `powershell -NoProfile -ExecutionPolicy Bypass -File ./verify.ps1` e mostre a saída real. Se falhar, pare, explique o erro e não prossiga para o commit.
3. Rode `git diff --stat` e resuma a mudança em uma ou duas frases.
4. Proponha a mensagem de commit e espere a aprovação:
   - inglês, no imperativo, primeira linha com até 72 caracteres;
   - prefixo `feat:`, `fix:`, `docs:`, `test:` ou `chore:`;
   - sem dado real de ocorrência;
   - termina com a linha de coautoria definida pelo ambiente.
5. Com a aprovação, faça `git add` listando cada arquivo pelo nome (nunca `git add .` nem `git add -A`) e `git commit`.
6. Mostre `git log --oneline -1` e `git status --short`.

Nunca faça `git push` sem pedido explícito. Não cite o caminho das planilhas reais em comandos: o hook do projeto bloqueia.
