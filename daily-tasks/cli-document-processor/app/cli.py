import argparse
import logging
from logger import setup_logger
from processor import process_folder

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Process files in a folder")
    parser.add_argument("folder", help="Folder path")

    args = parser.parse_args()

    logging.info("Starting file processing")
    results = process_folder(args.folder)

    logging.info("Processing completed")
    for file, count in results.items():
        print(f"{file}: {count} characters")


if __name__ == "__main__":
    main()