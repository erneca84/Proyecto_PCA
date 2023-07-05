##funciones sin nombre

def multiplica(a,b):
    resultado = a * b
    return resultado

result = multiplica(3,2)
print(result)

result_lambda = lambda a , b : a * b
print(result_lambda(3,4))

result_lambda_b = (lambda a,b : a * b) (5,1)
print(result_lambda_b)