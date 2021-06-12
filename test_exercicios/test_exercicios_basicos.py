import pytest
from Exercícios.romeu_e_julieta import romeu_e_julieta


def test_romeu_e_julieta_retorna_queijo():
    entrada = 3
    esperado = 'Queijo'
    resultado = romeu_e_julieta(entrada)
    assert resultado == esperado
