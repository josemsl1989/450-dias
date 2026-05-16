# Clasificador tonto de elementos por altura (en metros)
altura = 2.6  # cambia este valor y vuelve a ejecutar

if altura < 1.0:
    categoria = "Mobiliario bajo"
elif altura < 2.2:
    categoria = "Mobiliario alto / puerta estándar"
elif altura < 3.5:
    categoria = "Muro de planta"
else:
    categoria = "Elemento de doble altura"

print(f"Altura {altura} m → {categoria}")