def romeu_e_julieta(entrada):
    """
    “Escreva um programa que imprima os números de 1 a 100. Mas para múltiplos de três imprima
    ‘Fizz’ em vez do número e para os múltiplos de cinco imprima ‘Buzz’.
    Para números que são múltiplos de três e cinco imprimir ‘FizzBuzz'”.

    >>> romeu_e_julieta(20)
    1
    2
    Queijo
    4
    Goiabada
    Queijo
    7
    8
    Queijo
    Goiabada
    11
    Queijo
    13
    14
    Romeu e Julieta
    16
    17
    Queijo
    19
    Goiabada

    """

    n = entrada
    if n % 5 == 0 and n % 3 == 0:
        return('Romeu e Julieta')
    elif n % 5 == 0:
        return('Goiabada')
    elif n % 3 == 0:
        return('Queijo')
    else:
        return(n)

if __name__ == '__main__':
    romeu_e_julieta(100)
