def somarDoisNumeros(a,b):
    resultado = a + b
    return resultado

def triplo(soma):
    resultado = 3 * soma
    return resultado

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

soma = somarDoisNumeros(a,b)
triplicado = triplo(soma)

print("Soma: ",soma)
print("Multiplicado: ",triplicado)