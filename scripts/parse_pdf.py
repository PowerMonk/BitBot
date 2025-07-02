import pdfplumber
import re
from pathlib import Path


def extraer_insumos_pdf(path_pdf: Path) -> list[dict]:
    insumos = []

    with pdfplumber.open(path_pdf) as pdf:
        for i, page in enumerate(pdf.pages):
            texto = page.extract_text()
            if texto:
                lineas = texto.split('\n')

                for linea in lineas:
                    # Este patrón lo afinamos después, por ahora detecta nombres de insumos con % y dosis
                    if re.search(r"(FUNGICIDA|INSECTICIDA|NUTRICION).*?\d+(\.\d+)?", linea, re.IGNORECASE):
                        insumos.append(linea.strip())

    return insumos
