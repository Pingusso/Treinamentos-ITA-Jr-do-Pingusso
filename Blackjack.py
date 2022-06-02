import random

figuras = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
valor_carta = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class CARTA(object):
    def __init__(self, figura, naipe):
        self.figura = figura
        self.naipe = naipe

    """def qualnaipe(self):
        return self.naipe

    def qualfigura(self):
        return self.figura"""

    def __str__(self):
        return self.figura + ' ' + self.naipe

    def draw(self):
        print(self.figura + ' ' + self.naipe)


class MAO(object):
    def __init__(self):
        self.cartas = []
        self.valor = 0
        self.AS = False

    def __str__(self):
        mao_jogador = ""

        for carta in self.cartas:
            carta_nome = carta.__str__()
            mao_jogador += carta_nome

        return 'Sua mão é: {}'.format(mao_jogador)

    def puxarcarta(self, carta):
        self.cartas.append(carta)

        if carta.figura == 'A':
            self.AS = True
        self.valor += valor_carta[carta.figura]

    def somafinal(self):
        if self.AS is True and self.valor < 12:
            return self.valor + 10

        else:
            return self.valor

    def draw(self):
        for x in range(0, len(self.cartas)):
            self.cartas[x].draw()


"""class APOSTADOR(object):
    def __init__(self, saldo):
        self.saldo = saldo"""


class BARALHO(object):
    def __init__(self):
        self.baralho = []

        for naipe in naipes:
            for figura in figuras:
                self.baralho.append(CARTA(figura, naipe))

    def embaralhar(self):
        random.shuffle(self.baralho)

    def entregar(self):
        carta_topo = self.baralho.pop()
        return carta_topo


def fazeraposta():
    global aposta
    aposta = 0
    if saldo == 0:
        print('Você esta sem fichas')
        exit()

    print('Quanto deseja apostar?: ')
    while aposta == 0:
        entrada = input()
        entrada = int(entrada)
        if 1 <= entrada <= saldo:
            aposta = entrada
        else:
            print("Aposte menos! Você possui apenas {} fichas".format(saldo))


def entregar_cartas():
    global resultado, playing, baralho, mao_jogador, mao_dealer, saldo, aposta

    # Criando baralho
    baralho = BARALHO()
    baralho.embaralhar()

    fazeraposta()

    mao_dealer = MAO()
    mao_jogador = MAO()

    # Entregar 2 cartas para o jogador
    mao_jogador.puxarcarta(baralho.entregar())
    mao_jogador.puxarcarta(baralho.entregar())
    # Entregar 2 cartas para o dealer
    mao_dealer.puxarcarta(baralho.entregar())
    mao_dealer.puxarcarta(baralho.entregar())

    resultado = 'Hit(h) ou Stand(s)? '

    playing = True
    prosseguir()


def hit():
    global playing, saldo, baralho, mao_jogador, mao_dealer, aposta, resultado

    if playing:
        if mao_jogador.somafinal() <= 21:
            mao_jogador.puxarcarta(baralho.entregar())
        if mao_jogador.somafinal() >= 21:
            resultado = 'Se fudeu'
            saldo -= aposta
            playing = False
    else:
        resultado = 'Você não pode hitar!'

    prosseguir()


def stand():
    global playing, saldo, baralho, mao_jogador, mao_dealer, resultado, aposta

    if playing:
        while mao_dealer.somafinal() < 17:
            mao_dealer.puxarcarta(baralho.entregar())

        if mao_dealer.somafinal() > 21:
            resultado = 'A casa perdeu!'
            saldo += aposta

        elif mao_dealer.somafinal() < mao_jogador.somafinal():
            resultado = 'Você venceu a casa!'
            saldo += aposta

        elif mao_dealer.somafinal() == mao_jogador.somafinal():
            resultado = 'Emapate'

        else:
            resultado = 'A casa ganha'
            saldo -= aposta

        playing = False

    else:
        if mao_jogador.somafinal() > 0:
            resultado = 'Não é possível o Stand!'

    prosseguir()



def prosseguir():
    print('')
    print('A mão do jogador é: ')
    mao_jogador.draw()
    print('Sua mão vale: ' + str(mao_jogador.somafinal()))

    print('')
    print('A mão do dealer é: ')
    mao_dealer.draw()
    print('Sua mão vale: ' + str(mao_dealer.somafinal()))

    if playing == False:
        print('Salto atual: {} fichas'.format(saldo))

    print('-' * 20)
    print(resultado)
    if playing == False:
        print('Deal(d) ou Exit(e):')
    decisao()
    print('-' * 20)


def decisao():
    dec = input().lower()

    if dec == 'h':
        hit()
    elif dec == 's':
        stand()
    elif dec == 'd':
        entregar_cartas()
    elif dec == 'e':
        print('Obrigado por jogar')
        exit()
    else:
        print('Insira uma opção válida (h, s, d ou e): ')
        decisao()


# Entrando no jogo
print('Deseja entrar com quantas fixas? ')
saldo = input()
saldo = int(saldo)

# O JOGO EM SI
print('Bem vindo ao Blackjack')

baralho = BARALHO()
baralho.embaralhar()

mao_jogador = MAO()
mao_dealer = MAO()

entregar_cartas()
