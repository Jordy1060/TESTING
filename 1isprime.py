import math

import math

# Versión original (tiene error de v9)
def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):
        if (number % check) == 0:
            return False
    return True

# Versión corregida
def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):  
        if number % check == 0:
            return False
    return True

# Función de prueba
def test():
    # Tests para isPrime (función con error)
    print("Pruebas con isPrime (original):")
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    assert isPrime(9) == False  #  Este test falla con isPrime

    # Tests para isPrime2 (función corregida)
    print("Pruebas con isPrime2 (corregida):")
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(4) == False
    assert isPrime2(5) == True
    assert isPrime2(9) == False  # ✅ Correcto con isPrime2
    assert isPrime2(23) == True
    assert isPrime2(25) == False
    assert isPrime2(97) == True
    print("✅ Todas las pruebas pasaron correctamente.")

# Ejecutamos las pruebas
test()
