def primo(num):
    """
    :param num: numero
    :return: verificar se é primo
    """
    for n in range(2, num):
        if num % n == 0:
            print('Não é primo')
            break
    else:
        print("É primo")



numero = int(input('Insira um numero: '))
primo(numero)
