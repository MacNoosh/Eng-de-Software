def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)
resultado_potencia = potencia(2, 3)
print(f"2^3 = {resultado_potencia}")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
resultado_de_fibonacci = fibonacci(1)
print(f"O 5º termo da sequência de Fibonacci é {resultado_de_fibonacci}")


def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)
resultado_contar_digitos = contar_digitos(12345)
print(f"O número 12345 tem {resultado_contar_digitos} dígitos")


def palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindromo(s[1:-1])
resultado_do_palindromo_1 = palindromo("Renner")
resultado_do_palindromo_2 = palindromo("osso")
print(f"'Renner' é um palíndromo? {resultado_do_palindromo_1}")
print(f"'ossos' é um palíndromo? {resultado_do_palindromo_2}")


