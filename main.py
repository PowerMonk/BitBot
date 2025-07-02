from pathlib import Path
from scripts.parse_pdf import extraer_insumos_pdf

ruta_pdf = Path("data/entradas/Bit_Aplicaciones_Arturo_2022.pdf")
insumos = extraer_insumos_pdf(ruta_pdf)

print("\n--- INSUMOS DETECTADOS ---\n")
for i, linea in enumerate(insumos, start=1):
    print(f"{i}. {linea}")
