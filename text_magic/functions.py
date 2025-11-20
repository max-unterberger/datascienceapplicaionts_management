from string import punctuation


PUNCTUATION = punctuation + "“”"

def to_lower(text: str) -> str:
    return text.lower()

def clean_punctuation(text: str) -> str:
    output_string = ""
    for char in text:
        if char not in PUNCTUATION:
            output_string += char
    return output_string

def clean_strip(text: str) -> str:
        for _ in range(10):
            text = text.replace("  ", " ")  
        return text.strip()

def clean_stopwords(text: str, language:str="english") -> str:
    words = text.split(" ")
    for word in words:
        if word in stopwords.words(language):
            words.remove(word)

def pipeline(text:str) -> str:
    text = to_lower(text)
    text = clean_punctuation(text)
    text = clean_strip(text)
    return text