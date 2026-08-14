from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='ru', use_angle_cls=True)

def extract_passport_data(image_path):
    result = ocr.ocr(image_path, cls=True)
    
    # Собираем весь текст
    full_text = " ".join([line[1][0] for line in result[0]])
    
    # Простейший парсинг (можно заменить регулярками)
    data = {}
    # Пример: ищем "Серия" и берем следующие 2 слова
    # В реальности лучше использовать готовую либу "passport_reader" или парсить по маске
    if "серия" in full_text.lower():
        # ... логика извлечения
        pass
    return data