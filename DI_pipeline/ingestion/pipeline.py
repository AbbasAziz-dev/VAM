import os
import asyncio
from ingestion.models import DocumentOutput
from ingestion.readers import read_txt, read_pdf, read_docx
from ingestion.cleaner import clean_text


async def process_file(folder: str, filename: str) -> DocumentOutput | None:
    path = os.path.join(folder, filename)

    if filename.endswith(".txt"):
        raw = await read_txt(path)
        doc_type = "txt"
    elif filename.endswith(".pdf"):
        raw = await read_pdf(path)
        doc_type = "pdf"
    elif filename.endswith(".docx"):
        raw = await read_docx(path)
        doc_type = "docx"
    else:
        return None

    cleaned = clean_text(raw)
    words = cleaned.split()

    # Pydantic validation 
    return DocumentOutput(
        filename=filename,
        type=doc_type,
        word_count=len(words),
        content=cleaned
    )


async def ingest_documents(folder: str) -> list[DocumentOutput]:
    tasks = []

    for filename in os.listdir(folder):
        tasks.append(process_file(folder, filename))

    results = await asyncio.gather(*tasks)

    return [doc for doc in results if doc is not None]