import pytest

from src.math import soma


def test_deve_somar_dois_numeros_positivos():
    primeiro = 1
    segundo = 2
    result = soma(primeiro, segundo)
    expected = 3

    assert result == expected, f'Deve realizar a soma simples entre dois números positivos. Ex: {primeiro} e {segundo}'


def test_deve_somar_apenas_um_numero_e_retornar_ele_mesmo():
    given = 4
    result = soma(given)
    expected = given

    assert result == expected, 'Deve realizar a soma de um só número e retornar ele mesmo'


def test_nao_deve_ser_possivel_de_enviar_apenas_o_segundo_parametro():
    with pytest.raises(TypeError) as error:
        soma(b=2)

    assert "required positional argument: 'a'" in str(error.value)
