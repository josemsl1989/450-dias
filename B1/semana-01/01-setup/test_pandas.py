import pandas as pd

datos = {
    "elemento": ["Muro", "Puerta", "Ventana", "Suelo"],
    "cantidad": [120, 35, 48, 22],
    "nivel": ["P0", "P0", "P1", "P0"]
}

df = pd.DataFrame(datos)

print(df)
print("\nTotal elementos:", df["cantidad"].sum())
print("\nElementos en P0:")
print(df[df["nivel"] == "P0"])