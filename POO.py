class Dog(object):
    def __init__(self, raca,):
        self.raca = raca
    def latir(self):
        print('Auuuuuuu')

Sam = Dog(raca='Labrador')
print(Sam.raca)             #Printa a raça
Sam.latir()                 #Executa o latido


class Circulo(object):
    # pi = 3.1415
    def __init__(self, raio=1):
        self.raio = raio
    def area(self):
        pi = 3.1415
        return self.raio **2 * pi

    def defRAIO(self, raio):
        self.raio = raio


c = Circulo(2)
print(c.raio)
print(c.area())
c.defRAIO(3)
print(c.raio)
print(c.area())


class Animal(object):
    def __init__(self):
        print('Animal criado')

    def quemSouEu(self):
        print('Eu sou um animal')

    def comer(self):
        print('Nham Nham')


animalzinho = Animal()
animalzinho.quemSouEu()
animalzinho.comer()

# Herança
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado')
    def latido(self):
        print('AOUAOUUAOUAOUAOUAOU')


Bethoven = Cachorro()
Bethoven.comer()
Bethoven.latido()

# Metodos especiais
class Book(object):
    def __init__(self, titulo, autor, paginas):
        print('Um livro foi criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return 'Titulo: {}'.format(self.titulo)

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Livro destruido')


Livro = Book('Economia', 'Havard', 400)
print(Livro)
print(len(Livro))
nome = 'livrinho'
print(nome)


