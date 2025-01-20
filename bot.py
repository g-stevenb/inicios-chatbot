from sentence_transformers import SentenceTransformer, util
import os

#modelo = SentenceTransformer('all-MiniLM-L6-v2')
modelo = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

manuales = {}

for archivo in os.listdir("embeddings/"):
    if archivo.endswith(".txt"):  # Solo procesa archivos .txt
        with open(f"embeddings/{archivo}", "r", encoding="utf-8") as file:
            texto = file.read()
        manuales[archivo.replace(".txt", "")] = {  # Cambia a clave basada en el nombre del archivo
            "texto": texto,
            "embeddings": modelo.encode(texto.split("\n"), convert_to_tensor=True)
        }


def buscar_respuesta(pregunta, nivel):
    if nivel not in manuales:
        return (f"No se encontro un manual para el nivel '{nivel}'")

    texto = manuales[nivel]["texto"]
    embeddings = manuales[nivel]["embeddings"]

    embedding_pregunta = modelo.encode(pregunta, convert_to_tensor=True)

    similitudes = util.cos_sim(embedding_pregunta, embeddings)
    indice_respuesta = similitudes.argmax().item()

    lineas = texto.split("\n")
    inicio = max(0, indice_respuesta - 2)  # Dos líneas antes
    fin = min(len(lineas), indice_respuesta + 3)  # Dos líneas después
    respuesta = "\n".join(lineas[inicio:fin]).strip()  # Combinar líneas relacionadas
    return respuesta



if __name__ == "__main__":
    while True:
        nivel = input(
            "Cual es el nivel de pregunta: (vpn , metodologia, preguntas, django)")
        pregunta = input("Haz tu pregunta: ").strip()
        respuesta = buscar_respuesta(pregunta, nivel)
        print(f"Respuesta: {respuesta}")
