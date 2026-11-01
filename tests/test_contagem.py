from pathlib import Path

from resumo.contagem import contar_chamadas, formatar_resumo

FIXTURE = Path(__file__).parent / "fixtures" / "exemplo.csv"


def test_total_conta_todas_as_linhas():
    total, _ = contar_chamadas(FIXTURE.read_bytes())
    assert total == 6


def test_categoria_e_a_primeira_letra_da_natureza():
    _, categorias = contar_chamadas(FIXTURE.read_bytes())
    assert categorias == {"A": 2, "P": 3, "R": 1}


def test_letra_minuscula_vira_maiuscula():
    conteudo = "Natureza\r\np01 - teste\r\nP02 - teste\r\n".encode("cp1252")
    _, categorias = contar_chamadas(conteudo)
    assert categorias == {"P": 2}


def test_categorias_em_ordem_alfabetica():
    _, categorias = contar_chamadas(FIXTURE.read_bytes())
    assert list(categorias) == ["A", "P", "R"]


def test_le_acentos_do_windows_1252():
    conteudo = "Natureza\r\nÁ01 - INCÊNDIO\r\n".encode("cp1252")
    _, categorias = contar_chamadas(conteudo)
    assert categorias == {"Á": 1}


def test_formato_do_resumo():
    total, categorias = contar_chamadas(FIXTURE.read_bytes())
    assert formatar_resumo(total, categorias) == "Total: 6\nA - 2\nP - 3\nR - 1"
