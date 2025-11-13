# RAG Repository

This repository contains **RAG (Retrieval-Augmented Generation)** implementations using Google Gemini API.

You can download the code and files, and use them to:

- Upload documents (PDF, TXT, DOCX, JSON).
- Automatically convert documents into embeddings.
- Query your documents interactively to get grounded answers.

## Features

- Simple setup for RAG system.
- Interactive user query interface.
- Supports multiple document formats.
- No need to manage your own vector database.

## Usage

1. Clone or download this repository.
2. Place your documents in the `data` folder.
3. Configure your `.env` file with your Gemini API key.
4. Run the main Python script and interact with your documents.

## Prerequisites

- Python 3.8+
- Dependencies:

```bash
pip install google-genai python-dotenv
```

- `.env` file containing:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Notes

- Supported file types: PDF, TXT, DOCX, JSON.
- You can extend the scripts to multiple files or add chat-style memory.

Enjoy building RAG systems easily!
