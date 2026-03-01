from PyPDF2 import PdfReader
reader= PdfReader("sample-1.pdf")
text=""

for page in reader.pages:
    text+= page.extract_text()

print(text)