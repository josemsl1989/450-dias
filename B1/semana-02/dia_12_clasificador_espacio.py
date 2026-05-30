# dia_12_clasificador_espacio.py
# Clasificador de espacios de un proyecto según su área.
# Combina if/elif/else, and/or, in y validación básica con try/except.

# --- Entrada del usuario ---
nombre = input("Nombre del espacio: ").strip()
area_str = input("Área en m² (número): ").strip()

# Validación 1: nombre no vacío
if not nombre:
    print("Error: el nombre no puede estar vacío.")
else:
    # Validación 2: área convertible a float
    try:
        area = float(area_str)

        # Validación 3: área > 0
        if area <= 0:
            print("Error: el área debe ser mayor que 0.")
        else:
            # --- Clasificación por área ---
            if area < 6:
                categoria = "Espacio no habitable"
            elif 6 <= area < 15:
                categoria = "Espacio reducido"
            elif 15 <= area < 40:
                categoria = "Espacio estándar"
            elif 40 <= area < 100:
                categoria = "Espacio amplio"
            else:
                categoria = "Espacio singular"

            # --- Regla adicional: aseos pequeños ---
            nombre_lower = nombre.lower()
            aviso_normativa = False
            if ("baño" in nombre_lower or "aseo" in nombre_lower) and area < 6:
                aviso_normativa = True

            # --- Salida ---
            print(f'"{nombre}" ({area} m²) → {categoria}')
            if aviso_normativa:
                print("Verificar normativa: aseos suelen requerir mínimo de superficie.")

    except ValueError:
        print("Error: el área debe ser un número.")