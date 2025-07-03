import pdfplumber
import re
import json
from pathlib import Path
from typing import Dict, List


def cargar_insumos() -> Dict[str, Dict]:
    """Carga los insumos desde el JSON y crea un hashmap para búsqueda rápida."""
    insumos_path = Path(__file__).parent.parent / "data" / "insumos.json"
    
    with open(insumos_path, 'r', encoding='utf-8') as file:
        insumos_data = json.load(file)
    
    # Crear hashmap con el nombre como clave y el insumo con fecha más antigua
    insumos_map = {}
    
    for insumo in insumos_data:
        nombre = insumo["nombre"].lower()
        
        if nombre not in insumos_map:
            insumos_map[nombre] = insumo
        else:
            # Si ya existe, concatenar el año al nombre y agregarlo al hashmap
            nombre_con_año = f"{nombre}_{insumo['año_venta']}"
            insumos_map[nombre_con_año] = insumo
    
    return insumos_map


def buscar_precio_insumo(nombre_insumo: str, insumos_map: Dict[str, Dict]) -> str:
    """Busca el precio de un insumo en el hashmap."""
    # Buscar coincidencia parcial en el nombre
    nombre_lower = nombre_insumo.lower()
    
    for nombre_key, insumo_data in insumos_map.items():
        if nombre_key in nombre_lower or any(word in nombre_lower for word in nombre_key.split()):
            precio_total = insumo_data["precio_unitario"] * insumo_data["cantidad"]
            return f" - ${precio_total:,.0f}/{insumo_data['cantidad']}{insumo_data['unidad']}"
    
    return " - Precio no encontrado"


def extraer_insumos_pdf(path_pdf: Path) -> List[str]:
    """Extrae insumos del PDF y agrega precios desde el JSON."""
    insumos = []
    insumos_map = cargar_insumos()

    with pdfplumber.open(path_pdf) as pdf:
        for i, page in enumerate(pdf.pages):
            texto = page.extract_text()
            if texto:
                lineas = texto.split('\n')

                for linea in lineas:
                    # Este patrón lo afinamos después, por ahora detecta nombres de insumos con % y dosis
                    if re.search(r"(FUNGICIDA|INSECTICIDA|NUTRICION).*?\d+(\.\d+)?", linea, re.IGNORECASE):
                        linea_limpia = linea.strip()
                        precio_info = buscar_precio_insumo(linea_limpia, insumos_map)
                        insumos.append(linea_limpia + precio_info)

    return insumos
