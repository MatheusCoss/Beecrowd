A,B,C = list(map(float,input().split()))

# A = BASE B=LADO C=ALTURA

PI = 3.14159

triangulo = (A * C) / 2
circulo = PI * (C ** 2)
trapezio = (A + B) / 2 * C
quadrado = B ** 2
retangulo = A * B

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")