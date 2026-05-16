# Conversiones explícitas
numero_texto = "42"
numero_real = int(numero_texto)
print(numero_real + 8)  # 50

# Conversión que falla a propósito
# Descoméntala, ejecuta, lee el error, vuelve a comentarla
# numero_malo = int("cuarenta y dos")

# Float a int (trunca, no redondea)
print(int(3.9))   # 3
print(round(3.9)) # 4

# Concatenar str con número da error → hay que convertir
edad = 33
print("Tengo " + str(edad) + " años")
print(f"Tengo {edad} años")  # más limpio