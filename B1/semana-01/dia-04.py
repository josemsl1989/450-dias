"""
Día 4: verificación del entorno.
Comprueba que pandas se importa y que Python ve el venv correcto.
"""
import sys
import pandas as pd

print(f"Python: {sys.version}")
print(f"Ejecutable: {sys.executable}")
print(f"Pandas versión: {pd.__version__}")

datos = pd.DataFrame({"dia": [1, 2, 3, 4], "completado": [True, True, True, True]})
print(datos)