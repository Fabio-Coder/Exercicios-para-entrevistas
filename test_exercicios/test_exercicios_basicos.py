import pytest

from Exercícios.maior_e_menor_de_3 import menor_de_3, maior_de_3
from Exercícios.romeu_e_julieta import romeu_e_julieta


def test_romeu_e_julieta_retorna_queijo():
    entrada = 3
    esperado = 'Queijo'
    resultado = romeu_e_julieta(entrada)
    assert resultado == esperado

def test_menor_de_3_retorna_o_menor_valor():
    assert menor_de_3(3,1,2) == 1

def test_maior_de_3_retorna_o_maior_valor():
    assert maior_de_3(3,1,2) == 3