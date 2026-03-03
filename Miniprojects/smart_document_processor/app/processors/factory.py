from pathlib import Path
from app.processors.pdf_processor import PDFProcessor
from app.processors.docx_processor import DOCXProcessor


def get_processor(file_path: Path):
    if file_path.suffix.lower() == ".pdf":
        return PDFProcessor()
    if file_path.suffix.lower() == ".docx":
        return DOCXProcessor()

    raise ValueError(f"Unsupported file type: {file_path.suffix}")