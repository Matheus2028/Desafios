import string

chave = 'DAVID'
texto = 'IMSORRY'
chave_repetida = chave.upper() * (len(texto)//len(chave) + 1)

a = list(string.ascii_uppercase)

result = dict(list(zip(a, list(range(0, 28)))))

def criptografa(cifra, letra):
    return (a[cifra:] + a[:cifra])[letra]

def descriptografa(cifra, letra):
    return a[(a[cifra:] + a[:cifra]).index(letra)]

res = [criptografa(result[chave_repetida[i]], result[x]) for i, x in enumerate(texto.upper())]

encriptado = ''
descriptado = ''

for x in res:
    encriptado = encriptado + x

res2 = [descriptografa(result[chave_repetida[i]], x) for i, x in enumerate(text.upper())]

for x in res2:
    descriptado = descriptado + x

print(encriptado)
print(descriptado)