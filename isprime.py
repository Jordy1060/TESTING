import math

# Versión original (contiene un error para algunos números como 9)
def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):
        if (number % check) == 0:
            return False
    return True

# Versión corregida: ahora verifica correctamente incluyendo la raíz cuadrada
def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):  # +1 para incluir sqrt(n)
        if number % check == 0:
            return False
    return True

# Función de prueba con división entre versión incorrecta y corregida
def test():
    # Parte A: Tests para la función original con fallo
    print("Pruebas con isPrime (original):")
    assert isPrime(1) == False
    assert isPrime(2) == True


    # Parte B: Tests para la función corregida
    print("\nPruebas con isPrime2 (corregida):")
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(4) == False
    assert isPrime2(5) == True
    assert isPrime2(9) == False   #pasa correctamente
    assert isPrime2(23) == True
    assert isPrime2(25) == False
    assert isPrime2(97) == True
    print("✅ Todos los tests pasaron con isPrime2.")

test()
