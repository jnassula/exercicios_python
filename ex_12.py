altura = float(input("Qual é sua altura? "))
gender = input("Qual é o seu gênero? ")

if gender.lower == "m":
    peso_ideal = (72.7 * altura) - 58
elif gender.lower == "f":
    peso_ideal = (62.1 * altura) - 44.7

    print("O seu peso ideal é {:.2f} quilogramas.".format(peso_ideal))

else:
    peso_ideal = 0
    print("Genero não definido!")
