import argparse
import asyncio
import json
import logging
from pathlib import Path
from .logging_config import setup_logging
from .processors.factory import get_processor


async def process_folder(folder_path: str):
    path = Path(folder_path)

    if not path.exists():
        raise FileNotFoundError("Folder not found")

    tasks = []

    for file in path.iterdir():
        if file.suffix.lower() in [".pdf", ".docx"]:
            processor = get_processor(file)
            tasks.append(processor.process(file))

    results = await asyncio.gather(*tasks)

    output_path = Path("output/results.json")
    output_path.parent.mkdir(exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump([r.model_dump() for r in results], f, indent=4)

    logging.info("Processing complete.")


def main():
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Folder containing PDF/DOCX files")
    args = parser.parse_args()

    asyncio.run(process_folder(args.folder))


if __name__ == "__main__":
    main()