def matem(operation_1):
    if operation_1 == "+":
        def suma(z, y):
            return z + y

        return suma
    if operation_1 == "-":
        def minus(z, y):
            return z - y

        return minus
    if operation_1 == "/":
        def delit(z, y):
            return z / y

        return delit
    if operation_1 == "*":
        def umnojit(z, y):
            return z * y

        return umnojit
    if operation_1 == "**":
        def stepen(z, y):
            return z ** y

        return stepen


my_number = matem("**")
print(my_number(4, 2))
print('---------------------------------------------------------------')

print('лямда')
f = lambda x, y: x ** y
print(f(4, 2))
print('функция def')


def f(x, y):
    return x ** y


print(f(4, 2))
print('---------------------------------------------------------------')


class Rect:

    def __init__(self, dlina, shirina):
        self.a = dlina
        self.b = shirina

    def __call__(self):
        return self.a * self.b


Ploshad = Rect(5, 6)
print(Ploshad())
