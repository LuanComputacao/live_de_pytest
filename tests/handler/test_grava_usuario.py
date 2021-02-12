import csv

from src.handler import grava_usuario
from tests.handler.helpers import count_people_by_name


def test_deve_salvar_um_usuario_no_arquivo_csv(arquivo_de_usuarios, usuario_fake):
    given = usuario_fake()
    grava_usuario(**given, filename=arquivo_de_usuarios)
    result = count_people_by_name(given['nome'], arquivo_de_usuarios)
    expected = 1

    assert result == expected
