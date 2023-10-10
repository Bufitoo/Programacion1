
#El error estaba en las funciones most y least, ya q en vez de usar a y b q son los argumentos q recibe, estaba utilizando x y y
def most(a,b):
    if(a>b):
        return a
    else:
        return b
def least (a,b):
    if(a<b):
        return a
    else:
        return b
#Principal
x = int(input("Un numero"))
y = int(input("Otro numero"))

print(most(x-3, least(x+2, y-5)))