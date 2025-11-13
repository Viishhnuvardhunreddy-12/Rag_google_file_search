# Gemini RAG App

This repository demonstrates how to use **Google Gemini’s File Search** API to create a **Retrieval-Augmented Generation (RAG)** system in Python. With this app, you can upload documents and ask questions to get grounded answers automatically.

---

## Features

- Upload PDF, TXT, DOCX, or JSON files.
- Automatic embedding & chunking of uploaded documents.
- Query documents interactively using the console.
- RAG answers without managing your own vector database.

---

## Prerequisites

- Python 3.8+
- Google Gemini API key
- Dependencies:

```bash
pip install google-genai python-dotenv
```

- `.env` file in the project root containing:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## Project Structure

```
project/
├── data/
│   └── document.pdf       # Your document(s) go here
├── .env                   # API key file
└── gemini_rag.py          # Main Python script
```

---

## Usage

1. **Place your document** inside the `data` folder.
2. **Run the Python script**:

```bash
python gemini_rag.py
```

3. **Interact with the app**:

```
💬 Enter your question (or type 'exit' to quit): Summarize the document
```

The app will return a RAG-style answer based on your uploaded document.

---

## Code Overview

- **Upload file**: Converts the document into embeddings and stores it in a File Search Store.
- **Query file**: Gemini automatically retrieves relevant chunks and generates grounded answers.
- **Interactive loop**: Keep asking questions until you type `exit`.

---

## Notes

- Supported file types: PDF, TXT, DOCX, JSON
- Ensure your `.env` file is loaded correctly with your API key.
- You can upload multiple documents to the same File Search Store.

---

## Future Improvements

- Support for multiple file uploads automatically.
- Chat-style memory to remember previous questions and answers.
- Web interface integration.
