# AskAboutMe

A personal AI chatbot that answers questions about me using RAG powered by Qwen3 and LlamaIndex, running fully locally via Ollama.

## How it works

1. Loads my personal details from a text file
2. Converts them into searchable embeddings using `mxbai-embed-large`
3. When you ask a question, it finds the relevant part
4. Passes it to `Qwen3` to generate a natural answer

## Tech Stack

- **LLM:** Qwen3 (via Ollama)
- **Embeddings:** mxbai-embed-large (via Ollama)
- **RAG Framework:** LlamaIndex
- **Language:** Python

## Prerequisites

- Python 3.12+
- Ollama running with the following models pulled:
  - `qwen3:latest`
  - `mxbai-embed-large:latest`

## Setup

1. Clone the repository

```bash
   git clone https://github.com/KhadkaRipesh/my-assistant
   cd my-assistant
```

2. Create and activate virtual environment

```bash
   python -m venv venv
   source venv/bin/activate        # Linux/Mac
   venv\Scripts\activate           # Windows
```

3. Install dependencies

```bash
   pip install -r requirements.txt
```

4. Create `.env` file

5. Add your details in `data/my_details.txt`

6. Run the chatbot

```bash
   python main.py
```

## Usage

```
Chatbot ready! Type 'exit' to quit.

You: What are your skills?
Bot: Ripesh is skilled in Python, JavaScript, and React.

You: Where do you live?
Bot: Ripesh lives in Kathmandu, Nepal.

You: exit
Goodbye!
```

## Author

**Ripesh Khadka**

- GitHub: [KhadkaRipesh](https://github.com/KhadkaRipesh)
- Location: Kathmandu, Nepal
