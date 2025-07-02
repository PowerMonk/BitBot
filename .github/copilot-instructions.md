# Copilot Instructions

Este proyecto tiene como objetivo automatizar la creación de recetas y notas de venta agrícolas a partir de bitácoras en PDF.

## Objetivo

1. Leer archivos PDF que contienen bitácoras de aplicaciones de insumos agrícolas.
2. Extraer los datos relevantes de esas bitácoras (producto, dosis, fecha, etc.).
3. Calcular cantidades por hectárea y por huerta.
4. Llenar automáticamente una plantilla de Excel con receta y nota de venta.
5. Exportar el resultado en formato Excel y/o PDF.

## Consideraciones

- El PDF contiene tablas con formato fijo, pero hay información irrelevante que debe ignorarse.
- El archivo Excel base tiene dos hojas: una para la receta, otra para la nota de venta.
- Los productos se pueden cruzar con una base de datos local (`insumos.json`) para obtener precios.

## Tecnologías

Este es un proyecto Python local. Se usará:

- `pdfplumber` para leer PDFs
- `pandas` para manipular tablas
- `openpyxl` para trabajar con Excel
- `tkinter` para una interfaz gráfica

## Estructura esperada

recetador_agricola/
├── data/ # Datos de entrada y configuraciones
│ ├── insumos.json # Precios e info de insumos
│ └── entradas/ # Bitácoras de test en PDF
├── plantillas/ # Plantilla de Excel para las recetas y notas
│ └── receta_base.xlsx
├── scripts/ # Scripts reutilizables (core del programa)
│ ├── parse_pdf.py # Lógica para leer y extraer info del PDF
│ ├── generar_receta.py # Llenado de Excel y cálculos
│ └── utils.py # Funciones auxiliares comunes
├── gui/ # Código de la interfaz gráfica
│ └── app.py # Archivo principal de la GUI
├── main.py # Entrada principal del programa (CLI o GUI)
├── requirements.txt
└── README.md
