from app.models.document import DocumentInput
from app.models.config import ProcessingConfig
from app.models.extraction import ExtractionResult


def get_user_input():
    doc_id = input("Enter document ID: ")
    text = input("Enter document text: ")
    source = input("Enter source (pdf/email/web): ")

    max_keywords = int(input("Max keywords: "))

    return doc_id, text, source, max_keywords


def main():
    doc_id, text, source, max_keywords = get_user_input()


    document = DocumentInput(
        doc_id=doc_id,
        text=text,
        source=source
    )

    config = ProcessingConfig(
        max_keywords=max_keywords
    )

    result = ExtractionResult(
        doc_id=document.doc_id,
        entities=["Invoice", "ABC Corp"] if config.extract_entities else None,
        keywords=(
            document.text.lower().split()[: config.max_keywords]
            if config.extract_keywords
            else None
        ),
        metadata={
            "language": config.language,
            "source": document.source
        },
        confidence_score=0.85
    )
    print("\n--- Result (JSON) ---")
    print(result.model_dump_json(indent=2))

if __name__ == "__main__":
    main()