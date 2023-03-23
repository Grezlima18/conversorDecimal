## 1120366 - Guilherme de Rezende Lima
## 1133554 - Vitor Almeida Machado

numeroInformado = int(input("Informe um número inteiro para converter-lo em bit: "))
numeroBinario = [1]

def dec2bin(x):
    s = []
    while x > 1:
        p, q = divmod(x, 2)
        x = p
        numeroBinario.append(q)
    for val in numeroBinario:
        s.append(str(val))
    y = ''.join(s)
    return y


print("Seu número em binário é", dec2bin(numeroInformado))