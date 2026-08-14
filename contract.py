import openai
from docxtpl import DocxTemplate

def fill_contract_with_ai(passport_data):
    # 1 вариант: просто подставить через шаблонизатор
    doc = DocxTemplate("template.docx")
    doc.render(passport_data)
    doc.save("filled_contract.docx")
    return "filled_contract.docx"

    # 2 вариант: если договор сложный, просим GPT переписать пункты
    # prompt = f"У меня есть паспортные данные: {passport_data}. Вставь их в текст договора: [текст договора]"
    # response = openai.ChatCompletion.create(...)