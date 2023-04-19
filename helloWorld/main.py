#DIFFERENTS TYPES OF VALUES
#primeiro_nome = "matheus"
#segundo_nome = "vitor"
#nome_completo = primeiro_nome +" "+ segundo_nome
#print("Hello "+nome_completo)
#print(type("Hello "+nome_completo))

#age = 21
#age += 8
#print("you age is: " + str(age))
#print(type(age))

#weight = 63.5
#print(weight)
#print(type(weight))
#print("your weight is: " + str(weight) + "KG")

#human = False
#print("are you a human: " + str(human))
#print(type(human))

#DECLARE DIFFERENT VARIABLES AT THE SAME LINE
#name = "matheus"
#age = 24
#attractive = True
#name, age, attractive = "matheus", 24, True
#print(name)
#print(age)
#print(attractive)

#DECLARE SAME VALUES TO DIFFERENT VARIABLES
#sponge_bob = patrick = sandy = squidward = 30
#print(sponge_bob)
#print(patrick)
#print(sandy)
#print(squidward)

#USEFUL METHODS
#name = "Matheus Vitor"
#print(len(name))
#print(name.find("t"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("t"))
#print(name.replace("s", "d"))
#print(name*3)

#type casting = convert the data type of a value to another data type
#x = 1.0001
#x = str(x)
#print(type(x))
#print(x)

#name = input("What is your mame?")
#age = int(input("How old are u?"))
#age += 1
#weight = float(input("What's your weight?"))
#print("Hello " + name)
#print("You are "+str(age)+" years old")
#print("You are "+str(weight)+ "KG")

#name = ""
#while len(name) == 0:
#    name = input("Enter your name: ")
#print("Hello Mr " + name)

#import time
#for seconds in range(1,10+1):
#    print(seconds)
#    time.sleep(1)
#print("Happy New Year!")

#row = int(input("How many rows?"))
#columns = int(input("How many columns?"))
#symbol = input("Which symbol?")
#for i in range(row):
#    for j in range(columns):
#        print (symbol, end = '')
#    print()

#for i in range(1,21):
#    if i == 13:
#        continue
#    else:
#        print(i)

#capitals = {"PE": "Recife",
#            "CE": "Fortaleza",
#            "RN": "Natal",
#            "BA": "Salvador"}
#for x,y in capitals.items():
#    print(x,y + ", ", end="")

#def hello(**kwargs):
#    print('Hello ', end='')
#    for i in kwargs.items():
#        print(i[1] + ' ', end='')
#hello(first = 'Bro', middle ='Fernandes', last ='Moreira')

#text = "This is {} as {} are."
#print(text.format("me","you"))

#pi = 3.14159
#print("There is nothing so big as {:.2f}".format(pi))