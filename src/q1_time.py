from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer el archivo JSON en formato línea por línea
    df = pd.read_json(file_path, lines=True)
    print("Total tweets cargados:", len(df))

    # Convertir la columna 'date' de string a datetime.date
    df["date"] = pd.to_datetime(df["date"]).dt.date
    print("Fechas convertidas, ejemplo:", df["date"].iloc[0])

    # Extraer el nombre de usuario desde el diccionario 'user'
    df["user"] = df["user"].apply(lambda u: u["username"])
    print("Usuario ejemplo:", df["user"].iloc[0])

    # Agrupar los tweets por fecha y contar la cantidad por día
    tweet_counts = df.groupby("date").size().reset_index(name="count")
    print("Fechas únicas:", tweet_counts.shape[0])

    # Obtener las 10 fechas con mayor cantidad de tweets
    top10_dates = tweet_counts.nlargest(10, "count")["date"]
    print("Top 10 fechas:", top10_dates.tolist())

    # Filtrar el DF original para quedarnos solo con tweets de esas 10 fechas
    df_top = df[df["date"].isin(top10_dates)]
    print("Tweets filtrados por fechas top:", len(df_top))

    top_users_by_day = (
        df_top.groupby(["date", "user"])
        .size()
        .reset_index(name="count")
        .sort_values(["date", "count"], ascending=[True, False])
        .drop_duplicates("date")
    )

    return [(row["date"], row["user"]) for _, row in top_users_by_day.iterrows()]
