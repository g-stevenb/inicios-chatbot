import fitz

def extraer_texto(pdf_path):
    texto = ""
    with fitz.open(pdf_path) as pdf:
        for pagina in pdf:
            texto += pagina.get_text() + "\n"

    return unir_parrafos(texto)

def unir_parrafos(texto):
    lineas = texto.split("\n")
    parrafos = []
    parrafo_actual = ""

    for linea in lineas:
        if linea.strip():  # Si la línea no está vacía
            parrafo_actual += " " + linea.strip()
        else:  # Línea vacía indica final del párrafo
            if parrafo_actual:
                parrafos.append(parrafo_actual.strip())
                parrafo_actual = ""

    # Agregar el último párrafo si existe
    if parrafo_actual:
        parrafos.append(parrafo_actual.strip())

    return "\n\n".join(parrafos)

def guardar_texto(nombre_manual, texto):
    with open(f"embeddings/{nombre_manual}.txt", 'w', encoding="utf-8") as file:
        file.write(texto)

if __name__ == "__main__":
    manuales = {
        "vpn": "manuales/Manual-vpn.pdf",
        "metodologia": "manuales/Manual-metodologia-software.pdf",
        "preguntas": "manuales/Manual-preguntas.pdf",
        "django": "manuales/Manual-libro-django.pdf",
    }

    for nombre, ruta in manuales.items():
        texto = extraer_texto(ruta)
        guardar_texto(nombre, texto)
        print(f"Texto extraído y guardado para {nombre}")

"""
Instalamos pymupdf -> py -m pip install pymupdf


import fitz

def extraer_text(pdf_path):
    texto =''
    with fitz.open(pdf_path) as pdf:
        for pagina in pdf:
            texto += pagina.get_text()
        return texto

def guardar_texto(nombre_manual,texto):
    with open(f"embeddings/{nombre_manual}.txt",'w',encoding="utf-8") as file:
        file.write(texto)
        
if __name__ =="__main__":
    manuales = {
        "vpn":"manuales/Manual-vpn.pdf",
        "metodologia":"manuales/Manual-metodologia-software.pdf",
        "preguntas":"manuales/Manual-preguntas.pdf",
        "django":"manuales/Manual-libro-django.pdf",
    }
    
    
    for nombre, ruta in manuales.items():
        text = extraer_text(ruta)
        guardar_texto(nombre,text)
        print(f"Texto extraido y guardado para {nombre}")
"""