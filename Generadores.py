def numero(n):
    for i in range(n):
        print(i)

numb_funt = numero(10)        
#print(numb_funt)


def generador_numero(n):
    for i in range(n):
        yield i

num_generado = generador_numero(10)
print(num_generado)
print(next(num_generado))
