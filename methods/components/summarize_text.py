def summarize_text(document_str:str) -> str:
    summarized_string = document_str.split(sep='. ')
    return summarized_string[0] + '.'