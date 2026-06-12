"""
Día 16 / 450 — Clasificador de nombres de vistas de Revit.

Convención asumida: DISCIPLINA_NIVEL_DESCRIPCION
Disciplinas válidas: ARQ, EST, MEP.
Nivel válido: tiene que empezar por "P" (P00, P01, PB, etc.).
"""

vistas = [
    "ARQ_P00_Planta_Cotas",
    "EST_P01_Planta_Estructura",
    "MEP_P02_Climatizacion",
    "ARQ_PB_Planta_Acabados",
    "arq_p01_alzado_norte",
    "EST_P03",
    "  MEP_P00_Saneamiento  ",
    "P01_Planta_General",
    "ARQ_P02_Seccion_AA",
    "MEP_P01_Electricidad",
    "ARQ_S01_Seccion_BB",
]

# Contadores por disciplina
arq = 0
est = 0
mep = 0
mal_formateadas = 0

for nombre in vistas:
    # Normalizo: quito espacios y paso a mayúsculas para no depender del caso
    nombre_normalizado = nombre.strip().upper()
    partes = nombre_normalizado.split("_")

    # Necesito al menos DISCIPLINA_NIVEL_DESCRIPCION -> 3 trozos
    if len(partes) < 3:
        print("Aviso: vista mal formateada (faltan trozos) ->", nombre)
        mal_formateadas = mal_formateadas + 1
        continue

    disciplina = partes[0]
    nivel = partes[1]

    # Validación extra: el nivel tiene que empezar por "P"
    if not nivel.startswith("P"):
        print("Aviso: nivel no empieza por 'P' ->", nombre)
        mal_formateadas = mal_formateadas + 1
        continue

    if disciplina == "ARQ":
        arq = arq + 1
    elif disciplina == "EST":
        est = est + 1
    elif disciplina == "MEP":
        mep = mep + 1
    else:
        print("Aviso: disciplina no reconocida ->", nombre)
        mal_formateadas = mal_formateadas + 1

total = arq + est + mep + mal_formateadas

print()
print("Resumen de vistas")
print("- ARQ:", arq)
print("- EST:", est)
print("- MEP:", mep)
print("- Mal formateadas:", mal_formateadas)
print("Total procesadas:", total)