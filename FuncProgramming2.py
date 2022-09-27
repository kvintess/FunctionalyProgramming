class Multiply:

    def __init__(self, factor=2):
        self.factor = factor
    def __call__(self, *args):
        list= []
        for item in args:
            list.append(item * self.factor)
        return list
#my_example = Multiply(factor=5)
#result = my_example(1,2,3,4,5)
#print(result)

list_of_multip_objects=[]
for factor in (2,3,4,5):
    mult = Multiply(factor=factor)
    list_of_multip_objects.append(mult)
for mul in list_of_multip_objects:
    print(mul(10,20,30,40))