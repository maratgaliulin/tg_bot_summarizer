import pickle

def summarize_text(document_str:str) -> str:

    # Загрузка модели и токенизатора
    with open('methods/components/pickle_files/tokenizer_to_pickle.pkl', 'rb') as file:
        tokenizer = pickle.load(file)

    with open('methods/components/pickle_files/model_to_pickle.pkl', 'rb') as file:
        model = pickle.load(file)

    # Формирование запроса для суммаризации
    input_text = f"summarize: {document_str}"
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Получение суммаризации от модели
    outputs = model.generate(**inputs, max_length=50)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return result