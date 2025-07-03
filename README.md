---
title: Pdf Chat Rag
emoji: 🚀
colorFrom: blue
colorTo: blue
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: 🤖 PDF Chatbot with RAG + Pinecone + Mistral
license: mit
---

```markdown
# 📄 Chat with Your PDF – AI Assistant (RAG + FAISS + Mistral)

Upload a PDF and ask questions about its content.


This is a powerful PDF chatbot built using **Retrieval-Augmented Generation (RAG)** with **FAISS** for semantic search, **SentenceTransformers** for embeddings, and **Mistral AI** (Mistral model) for answering queries. The app is deployed using **Streamlit** on Hugging Face Spaces.

---

## 🚀 Features

- ✅ Upload any PDF
- ✅ Semantic chunking + embedding
- ✅ Instant answers via Mistral AI's LLMs
- ✅ FAISS-based similarity search
- ✅ Clean Streamlit UI
- ✅ Hugging Face Spaces integration (Docker)

---

## 🛠️ Tech Stack

- `Streamlit` – UI framework
- `SentenceTransformers` – For embedding PDF chunks
- `FAISS` – Fast similarity search
- `Mistral API` – LLMs (Mistral, etc.)
- `pypdf` – PDF text extraction
- `Docker` – Containerized deployment on Hugging Face

---

## 📂 Directory Structure

```

pdf-chat-rag/
│
├── src/
│   └── streamlit_app.py         # Main app code
├── requirements.txt             # Python dependencies
├── Dockerfile                   # For deployment to Hugging Face
└── README.md

````

---

## 🔧 Local Setup

```bash
git clone https://huggingface.co/spaces/rakshath6/pdf-chat-rag
cd pdf-chat-rag

# Optional: create a virtual environment
python3 -m venv venv && source venv/bin/activate

pip install -r requirements.txt

# Add your Mistral API key
echo "OPENROUTER_API_KEY=your-key-here" > .env

streamlit run src/streamlit_app.py
````

---

## 🧠 How It Works

1. PDF is uploaded → converted to raw text using `pypdf`
2. Text is chunked (300 tokens) and embedded using SentenceTransformer (`all-MiniLM-L6-v2`)
3. Chunks stored in a FAISS index
4. User asks a question → semantically matched with top chunks
5. Those chunks + user question are sent to Mistral API
6. Response is displayed!

---

## 🔐 Environment Variables

Place your Mistral AI API key in `.env`:

```env
OPENROUTER_API_KEY=your_key_here
```

---

## 📦 Requirements

`requirements.txt` includes:

```
streamlit
pypdf
sentence-transformers
faiss-cpu
openai
python-dotenv
```

---

## 🐳 Deployment on Hugging Face Spaces (Docker)

Ensure:

* Your app is in `src/streamlit_app.py`
* API key is added under **"Secrets"**
* No hardcoded `.env` file in repo

The app will auto-rebuild when pushed via Git or manually restarted.

---

## 🙌 Acknowledgments

* [Mistral](https://mistral.ai/)
* [Hugging Face Spaces](https://huggingface.co/spaces)
* [SentenceTransformers](https://www.sbert.net/)
* [FAISS](https://github.com/facebookresearch/faiss)

<!-- ---

## 📸 Preview

![screenshot](https://your-screenshot-url.com) optional

--- -->

## 📬 Contact

Created with ❤️ by [Rakshath U Shetty](https://github.com/rakshath6)

🔗 [Portfolio](https://rakshath66.github.io/portfolio/) / [LinkedIn](https://www.linkedin.com/in/rakshathushetty/) / [GitHub](https://github.com/rakshath6)

```

Let me know if you'd like me to customize:
- Your name / Hugging Face username
- Add a GIF demo
- Make it more startup-style or resume-portfolio style

Shall I save this to a file and commit it for you?
```


If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
