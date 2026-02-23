def clean_text(text):
    cleaned = ""

    for ch in text:
        if ch.isalnum():
            cleaned = cleaned + ch.lower()
        elif ch == " " or ch == "\n":
            cleaned = cleaned + " "

    return cleaned