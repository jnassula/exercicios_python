peso = float(input("Informe o peso do peixe: "))

if peso > 50:
    e = peso - 50
    m = e * 4

print("Peso: {:.2f}".format(peso))
print("Excesso: {}".format(e))
print("Multa: {}".format(m))
