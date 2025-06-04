from typing import List, Tuple
import json
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    # Procesa los tweets uno por uno para encontrar los 10 usuarios más mencionados,
    # No se guardan todas las menciones en una lista, se van sumando en el mismo momento que se recorre

    print(" Procesando menciones de usuarios Version Memoria")

    total_lines = 0
    counter = Counter()

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                total_lines += 1
                try:
                    tweet = json.loads(line)
                    mentioned = tweet.get("mentionedUsers", [])
                    if mentioned and isinstance(mentioned, list):
                        for user in mentioned:
                            username = user.get("username")
                            if username:
                                counter[username] += 1 # Se suman en el mismo momento las menciones, teniendo un contador
                except json.JSONDecodeError as decode_err:
                    print(f"Error en línea {total_lines}: {decode_err}")
                    continue
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
        return []

    top_10 = counter.most_common(10) # devuelve el top 10

    print(f"Total líneas leídas: {total_lines}")
    print(f"Usuarios únicos mencionados: {len(counter)}")
    print(f"Top 10 usuarios mencionados: {top_10}")

    return top_10