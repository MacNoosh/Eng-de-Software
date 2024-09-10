def fatorial(n):
    if n <0:
        return 'Não pode numero negativo!'
    contador_resultado = 1
    for i in range (1,n+1):
        contador_resultado *= i
    return contador_resultado

resultado = fatorial(5)
print(resultado)
    
