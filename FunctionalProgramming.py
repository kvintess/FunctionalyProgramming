#создадим функцию и класс, ведущий себя как функция
#def func(*args, **kwargs):
#    print(args, kwargs)

class Myfunction:

    def __call__(self, *args, **kwargs):
        print(args, kwargs)

func= Myfunction()
print(Myfunction)

func(a=2, b=3)
