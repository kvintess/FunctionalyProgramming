#создаем леммингов
import random

class Leming:
    total = 0

    def __init__(self):
        #обращаться через именование класса
        Leming.total += 1

family = []
family_size = random.randint(16,32)

while len(family) < family_size:
    new_leming = Leming()
    family.append(new_leming)
print(Leming.total)