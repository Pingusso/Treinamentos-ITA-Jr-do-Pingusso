l = [1, 2, 3, 4, 5]
l.append(6)
print('{} \n {}'.format(l, l.count(3)))

def square(num):
    return num **2


print("{}".format(square(25)))

# Funções lambda: apenas uma linha, nã necessãrio definir
quadrado = lambda num: num ** 2
print(quadrado(20))


