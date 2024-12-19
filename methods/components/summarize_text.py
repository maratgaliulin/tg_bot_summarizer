from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def summarize_text(document_str:str) -> str:

    # Загрузка модели и токенизатора
    tokenizer = AutoTokenizer.from_pretrained('cointegrated/rut5-base-multitask')
    model = AutoModelForSeq2SeqLM.from_pretrained('cointegrated/rut5-base-multitask')

    # Формирование запроса для суммаризации
    input_text = f"summarize: {document_str}"
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Получение суммаризации от модели
    outputs = model.generate(**inputs, max_length=50)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return result