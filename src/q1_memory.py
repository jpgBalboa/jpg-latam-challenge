from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
from dateutil import parser

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para contar tweets por fecha y por usuario
    date_user_count = defaultdict(lambda: defaultdict(int))
    total_lines = 0
    registros_ok = 0
    errores = 0

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            try:
                tweet = json.loads(line)

                # Verificamos que existan los campos clave antes de procesar
                if "date" not in tweet or "user" not in tweet or "username" not in tweet["user"]:
                    print(f"Línea {total_lines} con errores")
                    continue

                # Extraemos y parseamos los datos 
                raw_date = tweet["date"]
                username = tweet["user"]["username"]
                date = parser.isoparse(raw_date).date()

                # Incrementamos el conteo para esa fecha y usuario
                date_user_count[date][username] += 1
                registros_ok += 1

                if registros_ok % 10000 == 0:
                    print(f"{registros_ok} tweets procesados correctamente")

            except Exception as e:
                # En caso de error, mostramos información para depuración
                errores += 1
                print(f"Error en línea {total_lines}: {e}")
                print("Contenido:", line.strip())
                if errores >= 5:
                    print("Demasiados errores consecutivos, deteniendo ejecución.")
                    break

    # Resumen del procesamiento
    print("\nResumen del procesamiento")
    print(f"Líneas totales leídas: {total_lines}")
    print(f"Tweets válidos: {registros_ok}")
    print(f"Errores: {errores}")
    print(f"Fechas únicas encontradas: {len(date_user_count)}")

    # Obtenemos las 10 fechas con mayor volumen de tweets
    total_by_date = {d: sum(users.values()) for d, users in date_user_count.items()}
    top10_dates = sorted(total_by_date, key=total_by_date.get, reverse=True)[:10]
    print("Top 10 fechas con más tweets:", top10_dates)

    # Para cada fecha, seleccionamos el usuario con más tweets
    result = []
    for d in top10_dates:
        user_counts = date_user_count[d]
        if user_counts:
            top_user = max(user_counts.items(), key=lambda x: x[1])[0]
            result.append((d, top_user))

    return result