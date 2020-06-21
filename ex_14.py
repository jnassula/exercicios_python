valor_hora = 10.00
valor_hora_extra = 20.00

code = int(input("Digite o código do funcionário: "))
hours = float(input("Informe o número de horas trabalhadas: "))

if hours > 50:
    extra = (hours - 50) * valor_hora_extra
    payment = (50 * valor_hora) + extra
    print("Salário {:.2f}" .format(payment))
    print("Extra {:.2f}" .format(extra))

else:
    payment = (hours * valor_hora)
    print("Salário {:.2f}" .format(payment))
    print("Extra {:.2f}" .format(extra))

