import os
import logging

logger = logging.getLogger(__name__)
def process_file(filepath: str) -> int:
    logger.info(f"Processing file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return len(f.read())
    except UnicodeDecodeError:
        logger.error(f"Cannot decode file (not UTF-8): {filepath}")
        return 0


def process_folder(folder: str) -> dict:
    results = {}

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if os.path.isfile(path):
            results[filename] = process_file(path)

    return results