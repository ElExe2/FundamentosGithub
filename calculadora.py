#hola este es el primer dialogo

def suma (num1,num2):
    sum=num1+num2
    return sum

def calcularResta (num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacion (num1,num2):
    multi=num1*num2
    return multi

def calcularDivision (num1, num2):
    resultado = num1 / num2
    return resultado

while True:
    op=(int(input("ingrese la opcion que mas le corresponda\n1.suma\n2.resta\n3.division\n4.multiplicacion\n")))
    
    if op == 1:
        num1 = int(input('Ingrese el primer numero:\n'))
        num2= int(input('Ingrese el segundo numero:\n'))
        print(suma(num1, num2))