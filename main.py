from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
EMBED_MODEL = os.getenv("EMBED_MODEL")

Settings.llm = Ollama(
    model=MODEL_NAME,
    base_url=OLLAMA_URL,
    request_timeout=120.0
)

Settings.embed_model = OllamaEmbedding(
    model_name=EMBED_MODEL,
    base_url=OLLAMA_URL
)

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents)

chat_engine = index.as_chat_engine(
    chat_mode="condense_plus_context",
    system_prompt=(
        "You are a personal assistant. "
        "Only answer questions based on the provided context about this person. "
        "If the answer is not in the context, say 'I don't have that information.' "
        "Keep answers friendly and concise."
    )
)

print("Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = chat_engine.chat(user_input)
    print(f"\nBot: {response}\n")