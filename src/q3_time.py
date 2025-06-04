from typing import List, Tuple
import json
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:

    # Procesa todos los tweets para encontrar los 10 usuarios más mencionados,
    # Se cargan las menciones en all_mentions para luego realizar el conteo.

    print("Procesando menciones de usuarios Version Tiempo")

    total_lines = 0
    all_mentions = []

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
                                all_mentions.append(username) # Se almacenan las menciones
                except json.JSONDecodeError as decode_err:
                    print(f"Error en línea {total_lines}: {decode_err}")
                    continue
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
        return []

    counter = Counter(all_mentions) # se cuentan las menciones
    top_10 = counter.most_common(10)  # devuelve el top 10

    print(f"Total líneas leídas: {total_lines}")
    print(f"Usuarios únicos mencionados: {len(counter)}")
    print(f"Top 10 usuarios mencionados: {top_10}")

    return top_10