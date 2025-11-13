from google import genai
from google.genai import types
from dotenv import load_dotenv
import os, time

# 1️⃣ Load environment variables
load_dotenv()

# 2️⃣ Initialize Gemini client using API key from .env
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 3️⃣ Create File Search store
file_search_store = client.file_search_stores.create(
    config={'display_name': 'my-fileSearchStore'}
)
print("✅ File Search Store created!")

# 4️⃣ Upload your document (make sure it exists)
file_path = "data/document.pdf"  # Change extension if it's .txt or .docx

print(f"📤 Uploading file: {file_path}")
operation = client.file_search_stores.upload_to_file_search_store(
    file=file_path,
    file_search_store_name=file_search_store.name,
    config={'display_name': 'uploaded-document'}
)

# 5️⃣ Wait until upload + import completes
while not operation.done:
    print("⏳ Importing file... please wait...")
    time.sleep(5)
    operation = client.operations.get(operation)

print("✅ File imported successfully and ready for queries!\n")

# 6️⃣ Interactive user query loop
while True:
    user_query = input("💬 Enter your question (or type 'exit' to quit): ")

    if user_query.lower() == "exit":
        print("👋 Exiting the chat. Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_query,
        config=types.GenerateContentConfig(
            tools=[
                dict(file_search=dict(
                    file_search_store_names=[file_search_store.name]
                ))
            ]
        )
    )

    print("\n🧩 Gemini's Answer:\n")
    print(response.text)
    print("\n" + "-" * 60 + "\n")
