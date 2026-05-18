# dia_11_validador.py
# Validador de datos de un elemento BIM ficticio

nombre = input("Nombre del elemento: ").strip()
nivel_str = input("Nivel (número entero): ").strip()
categoria = input("Categoría (muro / suelo / pilar): ").strip().lower()
superficie_str = input("Superficie en m² (número): ").strip()

# Validación 1: nombre no vacío
if not nombre:
    print("Error: el nombre no puede estar vacío.")
# Validación 2: nivel convertible a entero
elif not nivel_str.lstrip("-").isdigit():
    print("Error: el nivel debe ser un número entero.")
else:
    nivel = int(nivel_str)
    # Validación 3: nivel en rango
    if not -5 <= nivel <= 50:
        print("Error: el nivel debe estar entre -5 y 50.")
    # Validación 4: categoría reconocida
    elif categoria not in ("muro", "suelo", "pilar"):
        print("Error: categoría no reconocida.")
    else:
        # Validación 5: superficie convertible a float y > 0
        try:
            superficie = float(superficie_str)
        except ValueError:
            print("Error: la superficie debe ser un número.")
        else:
            if superficie <= 0:
                print("Error: la superficie debe ser mayor que 0.")
            else:
                print(
                    f"OK -> {nombre} | nivel {nivel} | {categoria} | "
                    f"{superficie:.2f} m²"
                )