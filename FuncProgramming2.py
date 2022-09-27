class Multiply:

    def __init__(self, factor=2):
        self.factor = factor
    def __call__(self, *args):
        list= []
        for item in args:
            list.append(item * self.factor)
        return list
my_example = Multiply(factor=5)
result = my_example(1,2,3,4,5)
print(result)