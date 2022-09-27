#создаем леммингов
# import random
#
# class Leming:
#     total = 0
#
#     def __init__(self):
#         обращаться через именование класса
        # Leming.total += 1
#
# family = []
# family_size = random.randint(16,32)
#
# while len(family) < family_size:
#     new_leming = Leming()
#     family.append(new_leming)
# print(Leming.total)
import random
class leming:
    names = ['peter', 'july', 'alex', 'max']
    tail_lenght = 20
    total = 0

    def __init__(self):
        self.tail_lenght = random.randint(15, 25)
        self.name = random.choice(leming.names)
        leming.total = leming.total + 1

    def __str__(self):
        return 'name ' + self.name + ' tail lenght ' + str(self.tail_lenght)

borrow = []
borrow_depth = random.randint(90, 100)
while len(borrow) < borrow_depth:
    family = []
    family_size = random.randint(16, 32)
    while len(family) < family_size:
        new_lemming = leming()
        family.append(new_lemming)
    borrow.append(family)
print(leming.total)