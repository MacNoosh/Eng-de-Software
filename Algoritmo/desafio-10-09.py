import random
import string

def gerador_de_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def cifra_cesar(caractere, deslocamento):
    if caractere.isascii() and caractere.isprintable():
        return chr((ord(caractere) + deslocamento) % 256)
    return caractere

def criptografar_senha(senha, deslocamento):
    return ''.join(cifra_cesar(c, deslocamento) for c in senha)

# CONFIGURAR O TAMANHO E DESLOCAMENTO
tamanho_senha = 8  
deslocamento = 3   

senha_original = gerador_de_senha(tamanho_senha)
senha_criptografada = criptografar_senha(senha_original, deslocamento)

print(f"Senha original: {senha_original}")
print(f"Senha criptografada: {senha_criptografada}")
