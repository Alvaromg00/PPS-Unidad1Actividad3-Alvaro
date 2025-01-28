# Función calculadora
def calculadora():
    
    obtenerOperacion()

# Función para obtener el tipo de operación
def obtenerOperacion():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        operacion = input("Ingrese el número de la operación (1/2/3/4): ")
        
        if operacion in ['1', '2', '3', '4']:
            obtenerNumeros(operacion)
        elif operacion == '5':
            print("Saliendo de la calculadora...")
            break;
        else:
            print("Introduce una opción válida por favor!")

#Obtiene los números a operar
def obtenerNumeros(operacion):
    while True:
        num1 = input("Ingrese el primer número: ")
        if isNumber(num1):
            num1 = float(num1)
            while True:
                num2 = input("Ingrese el segundo número: ")
                if isNumber(num2):
                    num2= float(num2)
                    ejecutarOperacion(operacion, num1, num2)
                    break;
                else:
                    print("Introduce un número!")
            break;
        else:
            print("Introduce un número!")

#Dependiendo de la operación introducida llama a la función correspondiente y le pasa los números introducidos
def ejecutarOperacion(operacion, num1, num2):
    if operacion == '1':
        print("Resultado:", suma(num1, num2))
    elif operacion == '2':
        print("Resultado:", resta(num1, num2))
    elif operacion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif operacion == '4':
        print("Resultado:", division(num1, num2))
            
# Función que suma los números
def suma(a, b):
    return a + b

# Función que resta los números
def resta(a, b):
    return a - b;

# Función que multiplica los números
def multiplicacion(a, b):
    return a * b

# Función que divide los números
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Verifica si el valor es un número (entero o flotante)
def isNumber(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    calculadora()
