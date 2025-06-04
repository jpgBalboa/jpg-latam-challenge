import emoji
from typing import List

def extract_emojis(text: str) -> List[str]:
    """
    Extrae todos los emojis individuales de un texto usando la librería `emoji`.

    :param text: Texto desde el cual extraer emojis.
    :return: Lista de emojis encontrados.
    """
    return [char for char in text if char in emoji.EMOJI_DATA]