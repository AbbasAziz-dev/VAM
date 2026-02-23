from config import APP_NAME, INPUT_FILE
from processor import clean_text, word_count, char_count
from utils.file_handler import read_file, write_file

print(APP_NAME)

text = read_file(INPUT_FILE)

cleaned_text = clean_text(text)

words = word_count(cleaned_text)
chars = char_count(cleaned_text)

result = f"""Cleaned Text:
{cleaned_text}

Word Count: {words}
Character Count: {chars}
"""

write_file("output.txt", result)

print("Done")