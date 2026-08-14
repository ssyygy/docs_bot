import pytesseract
from PIL import Image

# Указываем язык распознавания (кириллица)
TESS_LANG = "rus"


def extract_passport_data(image_path):
    image = Image.open(image_path)

    full_text = pytesseract.image_to_string(image, lang=TESS_LANG)

    # Простейший парсинг (можно заменить регулярками)
    data = {}
    if "серия" in full_text.lower():
        # ... логика извлечения
        pass

    data["raw_text"] = full_text
    return data