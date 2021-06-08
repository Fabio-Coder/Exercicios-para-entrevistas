from maior_e_menor_de_3 import menor_de_3
def otimiza_corte():
    """
    Otimização de corte - Um marceneiro, para fazer um trabalho, precisa cortar vários pedaços demadeira de 45 cm
    cada um. Ele pode comprar tábuas de 3, 4 ou 5 metros. Usando os operadoresdiv e mod, faça um programa que calcule
    a quantidade de pedaços e a sobra para cada tipo detábua, permitindo assim uma melhor escolha do marceneiro.

    """

    unidade_tabua = 450
    tabua_3m = 3000
    tabua_4m = 4000
    tabua_5m = 5000

    sobra_tabua_3m = tabua_3m % unidade_tabua
    sobra_tabua_4m = tabua_4m % unidade_tabua
    sobra_tabua_5m = tabua_5m % unidade_tabua

    print(menor_de_3(sobra_tabua_3m,sobra_tabua_4m,sobra_tabua_5m))



if __name__ == '__main__':
    otimiza_corte()
