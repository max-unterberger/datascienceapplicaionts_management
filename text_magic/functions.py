def pipeline(text):
    def to_lowercase(text: str) -> str:
        return text.lower()

    def clean_punctuation(text: str) -> str:
        output_string = ""
        for char in text:
            if char not in PUNCTUATION:
                output_string += char
        return output_string

    text = to_lowercase(text)
    text = clean_punctuation(text)
    