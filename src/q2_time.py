from typing import List, Tuple
import json
from collections import Counter

# Se crea un py para utilizar la misma funcion de emojis en ambos ejercicios
from utils.emoji_utils import extract_emojis


def q2_time(file_path: str) -> List[Tuple[str, int]]:

    #Procesa el archivo línea por línea para encontrar los 10 emojis más usados.
    #Los emojis quedan almacenados en una lista

    print("Procesando emojis")

    all_emojis = []
    total_lines = 0

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                total_lines += 1
                try:
                    tweet = json.loads(line)
                    content = tweet.get("content", "")
                    emojis = extract_emojis(content)
                    all_emojis.extend(emojis) # Se almacenan en all_emojis
                except json.JSONDecodeError as decode_err:
                    print(f"Error en línea {total_lines}: {decode_err}")
                    continue
    except Exception as e:
        print(f"Error abriendo el archivo: {e}")
        return []

    counter = Counter(all_emojis) # se realiza el conteo de emojis
    top_10 = counter.most_common(10)

    print(f"Total líneas leídas: {total_lines}")
    print(f"Emojis únicos encontrados: {len(counter)}")
    print(f"Top 10 emojis: {top_10}")

    return top_10