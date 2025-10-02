# 📄 DocuChat – Chat with Your PDF using AI

DocuChat is an AI-powered PDF chatbot that allows you to upload any PDF and ask questions about it.  
It uses **Semantic Search + FAISS + OpenAI/OpenRouter LLMs** to provide accurate and contextual answers sourced directly from your document.

---

## 🚀 Features

✅ Upload any **PDF (text-based)**  
✅ **Chunking + Embedding** using SentenceTransformers  
✅ **Semantic search** using FAISS  
✅ Streamlit-based **Chat UI**  
✅ Uses **OpenRouter / OpenAI API** for responses

---

## 🛠️ Tech Stack

| Component            | Technology Used |
|----------------------|------------------|
| Frontend / UI        | Streamlit        |
| Embedding Model      | all-MiniLM-L6-v2 (SentenceTransformers) |
| Vector Store         | FAISS            |
| LLM (Chat Responses) | OpenRouter / OpenAI |
| PDF Parsing          | PyPDF            |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/DocuChat.git
cd DocuChat

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

🔑 Setup Environment Variables

Create a .env file in the project root and add:

OPENAI_API_KEY=your_openai_key
OPENROUTER_API_KEY=your_openrouter_key

▶️ Run the App
streamlit run src/streamlit_app.py


Then open the local URL in your browser:

http://localhost:8501

🧠 How It Works

Extracts text from PDF

Splits it into small chunks

Embeds and stores them in FAISS vector index

When you ask a question → retrieves the most relevant chunks

Sends them to the LLM to generate an answer

🤝 Contributing

Pull requests are welcome! Feel free to:

Add support for multiple PDFs

Use different models (like GPT-4, LLaMA, Mixtral)

Improve UI layout

📜 License

MIT License – Free to use and modify!
