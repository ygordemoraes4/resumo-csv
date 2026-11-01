import csv
import io
from collections import Counter

CODIFICACAO = "cp1252"
SEPARADOR = ";"
COLUNA_NATUREZA = "Natureza"


def contar_chamadas(conteudo: bytes) -> tuple[int, dict[str, int]]:
    """Conta as chamadas do CSV do CAD: total e quantidade por categoria.

    Toda linha conta como chamada atendida. A categoria é a primeira letra
    da coluna Natureza, em maiúscula.
    """
    texto = conteudo.decode(CODIFICACAO)
    leitor = csv.DictReader(io.StringIO(texto, newline=""), delimiter=SEPARADOR)
    categorias = Counter(linha[COLUNA_NATUREZA][0].upper() for linha in leitor)
    return categorias.total(), dict(sorted(categorias.items()))


def formatar_resumo(total: int, categorias: dict[str, int]) -> str:
    linhas = [f"Total: {total}"]
    linhas += [f"{letra} - {quantidade}" for letra, quantidade in categorias.items()]
    return "\n".join(linhas)
