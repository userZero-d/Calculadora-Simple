print ("Bienvenido a Calculadora, ¿Que desea hacer?")

#funcion que recibe y verifica el input
def get_input():
    userinput = "invalid"
    while userinput == "invalid":
        userinput = input("")
        if userinput.isupper() == True or userinput.islower() == True:
            print ("That is an invalid input. Try again:")
            userinput = "invalid"
        for n in range(0,len(userinput)):
            if userinput[n] in "Xx*/+-" and userinput[n+1] in "Xx*/+-":
                print ("That is an invalid input. Try again:")
                userinput = "invalid"
    return userinput

userinput = get_input()

#diccionarios definidos y variables de reserva "n" y "m" 
numbers = {1:""}
n = 1
m = 1

#bucle para convertir el input en variables utilizables en diccionarios
for char in userinput:
    if char in "0123456789":
        numbers[n] += char
    if char in "Xx*/+-":
        n += 1
        numbers[n] = ""
        numbers[n] = char
        n += 1
        numbers [n] = ""

#primer bucle for para la multiplicacion y la division
for key in numbers:
    z = 1
    o = 1
    if numbers[key] == "X" or numbers[key] == "x" or numbers[key] == "*":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) * int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""
    if numbers[key] == "/":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) / int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""
#segundo bucle para la suma y resta
for key in numbers:
    z = 1
    o = 1
    if numbers[key] == "+":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) + int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""
    if numbers[key] == "-":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) - int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""

#bucle que recorre el diccionario e imprime el número restante, que es la respuesta final
for key in numbers:
    if numbers[key] != "":
        print (str(userinput) + " = " + str(numbers[key]))

