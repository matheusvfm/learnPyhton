#contador = 0
#while contador < 5:
#    contador += 1
#    print(contador)
#    if contador == 5:
#        print("A dica é que é uma comida doce!")
#    else:
#        print()

name = 0
while name != "donut":
    name = input("Qual a comida preferida de Matheus?")
    name = name.lower()
    for i in name:
        if i == "d" and i == name[0]:
            print(i + " ✅")
        elif i == "d" and i != name[0]:
            print(i + " NÃO É NESSA LOCALIZAÇÃO")
        elif i == "o" and i == name[1]:
            print(i + " ✅")
        elif i == "o" and i != name[1]:
            print(i + " NÃO É NESSA LOCALIZAÇÃO")
        elif i == "n" and i == name[2]:
            print(i + " ✅")
        elif i == "n" and i != name[2]:
            print(i + " NÃO É NESSA LOCALIZAÇÃO")
        elif i == "u" and i == name[3]:
            print(i + " ✅")
        elif i == "u" and i != name[3]:
            print(i + " NÃO É NESSA LOCALIZAÇÃO")
        elif i == "t" and i == name[4]:
            print(i + " ✅")
        elif i == "t" and i != name[4]:
            print(i + " NÃO É NESSA LOCALIZAÇÃO")
        else:
            print(i + " NÃO PERTENCE A PALAVRA CHAVE.")

    if name == "donut":
        print("RESPOSTA CERTA")
    else:
        print()
