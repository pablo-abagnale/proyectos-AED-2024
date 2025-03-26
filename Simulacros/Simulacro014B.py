import random

# Semilla del generador
random.seed(49)

# Generar 20000 números aleatorios entre 1 y 45000
numeros = [random.randint(1, 45000) for _ in range(20000)]

# Verificar la suma de todos los números generados
suma = sum(numeros)
print(f"Suma de todos los números generados: {suma}")

# Contar cuántos números son múltiplos de 5, 7 y 9
multiplos_5 = len([num for num in numeros if num % 5 == 0])
multiplos_7 = len([num for num in numeros if num % 7 == 0])
multiplos_9 = len([num for num in numeros if num % 9 == 0])

print(f"Números múltiplos de 5: {multiplos_5}")
print(f"Números múltiplos de 7: {multiplos_7}")
print(f"Números múltiplos de 9: {multiplos_9}")