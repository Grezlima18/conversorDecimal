## 1120366 - Guilherme de Rezende Lima
## 1133554 - Vitor Almeida Machado

numeroInformado = int(input("Informe um número inteiro para converter-lo em bit: "))
numeroBinario = []


def dec2bin(x,y):
    while x > 0:
        p, q = divmod(x, 2)
        x = p
        y.append(q)
    y.reverse()
    return(y)


def list2int(s):
    v = []
    for g in range(0, len(s)):
        x = str(s[g])
        v.append(x)
    
    str1 = ""  
    for ele in v:
        str1 += ele
    return str1

dec2bin(numeroInformado, numeroBinario)

print("Seu número em binário é", list2int(numeroBinario))
