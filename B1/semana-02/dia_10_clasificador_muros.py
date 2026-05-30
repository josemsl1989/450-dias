# dia_10_clasificador_muros.py — Clasificador básico de muros con if/elif/else.
# Clasificador de muros en función de su espesor

espesor = 0.55      # en metros
material = "hormigon"
altura = 4.20       # en metros

# Clasificación por espesor y material
if espesor >= 0.20 and material == "hormigon":
    tipo = "estructural"
elif espesor < 0.15 and material in ("yeso", "ladrillo_hueco"):
    tipo = "divisorio"
else:
    tipo = "revisar"

print(f"Muro {tipo} | {espesor} m | {material}")

# Control de altura
if altura > 4.0:
    print("AVISO: altura no estándar, comprobar familia")
elif altura <= 0:
    print("ERROR: altura inválida")