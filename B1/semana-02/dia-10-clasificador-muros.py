espesor = 0.55      # en metros
material = "hormigon"
altura = 4.20       # en metros

# clasificación por espesor y material
if espesor >= 0.20 and material == "hormigon":
    tipo = "estructural"
elif espesor < 0.15 and material in ("yeso", "ladrillo_hueco"):
    tipo = "divisorio"
else:
    tipo = "revisar"

print(f"Muro {tipo} | {espesor} m | {material}")

# control de altura
if altura > 4.0:
    print("AVISO: altura no estándar, comprobar familia")
elif altura <= 0:
    print("ERROR: altura inválida")