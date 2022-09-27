#создаем леммингов
import random

class Leming:
    pass

total_lemings=0
family = []
family_size = random.randint(16,32)

while len(family) < family_size:
    new_leming = Leming()
    family.append(new_leming)
    total_lemings += 1
print(total_lemings)