def fizbuzz(intervalo):
    """
    “Escreva um programa que imprima os números de 1 a 100. Mas para múltiplos de três imprima
    ‘Fizz’ em vez do número e para os múltiplos de cinco imprima ‘Buzz’.
    Para números que são múltiplos de três e cinco imprimir ‘FizzBuzz'”.

    >>> fizbuzz(20)
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz

    """

    for n in range(1,intervalo + 1):
        if n % 5 == 0 and n % 3 == 0:
            print('FizzBuzz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 3 == 0:
            print('Fizz')
        else:
            print(n)

if __name__ == '__main__':
    fizbuzz(100)
