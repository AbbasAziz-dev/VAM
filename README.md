# VAM – Python Engineering for AI Systems

This repository contains my hands-on practice while learning the Python engineering concepts required to build **AI and LLM-based applications**.

The focus of this work is on writing **production-style Python code** including object-oriented design, async programming, API integration, data validation, testing, and CLI tools.

---

## Repository Structure

```
VAM
├── daily-tasks
└── Miniprojects
    └── smart_document_processor
```


- **daily-tasks** – Small implementations and exercises to practice core Python engineering concepts such as OOP, Pydantic models, async programming, API handling, and testing.

- **Miniprojects** – End deliverables where the learned concepts are combined into complete applications.

---

## Mini Project: Smart Document Processor

A CLI-based Python application that processes documents and outputs structured data.

Features:

- CLI interface using `argparse`
- OOP-based processor architecture
- Input/output validation using **Pydantic**
- Asynchronous processing for better performance
- API integration for text enrichment
- Structured JSON output
- Logging for debugging and monitoring
- Test suite using **pytest** with mocked API calls

---

## Technologies Used

- Python
- asyncio
- httpx
- Pydantic
- pytest
- argparse
- logging
