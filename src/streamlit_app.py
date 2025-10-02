# ✅ Streamlit Web App: PDF RAG Chatbot

# src/streamlit_app.py
import os
import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

import requests
# ─────────────────────────────────────────────────────────────
    
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# load_dotenv(dotenv_path=".env")
# api_key = os.getenv("OPENAI_API_KEY")
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "❌ No API key found! Set OPENROUTER_API_KEY (OpenRouter) or OPENAI_API_KEY in environment."
    )

# ✅ Set required env var
# os.environ["OPENAI_API_KEY"] = api_key

# Initialize OpenAI / OpenRouter client
if os.getenv("OPENROUTER_API_KEY"):
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
else:
    client = OpenAI(api_key=api_key)

# ✅ OpenRouter Client with headers for Hugging Face Spaces
# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=api_key,
#     default_headers={
#         "User-Agent": "hf-space-pdf-chat",
#         "HTTP-Referer": "https://huggingface.co/spaces/rakshath6/pdf-chat-rag",
#         "X-Title": "PDF Chat RAG Space"
#     }
# )
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

# ─── Embedding Model ───────────────────────────────────────────────────────────
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu") #device="cpu"
model.max_seq_length = 256  # Lower = less RAM use

# ─── Streamlit Layout ──────────────────────────────────────────────────────────
st.markdown(
    """
    <h1 style="
        background: linear-gradient(to right, red, orange, orange, red);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 3rem;
        text-align: center;
        padding: 1rem 0;
    ">
        📄 Chat with Your PDF
    </h1>
    
    """,
    unsafe_allow_html=True
)

uploaded = st.file_uploader("Upload a PDF", type="pdf")
if not uploaded:
    st.stop()

# ─── PDF → Text → Chunks → FAISS Index ──────────────────────────────────────────
# 1) Read PDF
reader   = PdfReader(uploaded)

# 2) Extract raw text
raw_text = "\n".join(p.extract_text() or "" for p in reader.pages)
if not raw_text.strip():
    st.warning("❗ No extractable text found in this PDF.")
    st.stop()

# 3) Chunking
def chunk_text(txt, size=300):
    words = txt.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

# enable the text_input now that parsing succeeded
# st.experimental_rerun()  # re-run so that the input box becomes enabled on next render

chunks     = chunk_text(raw_text)

# 4) Embed + FAISS index
embeddings = model.encode(chunks).astype("float32")
index      = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# ─── Chat History ───────────────────────────────────────────────────────────────
# 5) Chat history init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# ─── Retrieval + Generation ────────────────────────────────────────────────────
# 7) Semantic search helper
def semantic_retrieve(query, k=3):
    q_vec = model.encode([query]).astype("float32")
    _, I = index.search(q_vec, k)
    return [chunks[i] for i in I[0]]

# 8) Build prompt + payload
def generate_answer(question):
    context = "\n".join(semantic_retrieve(question))
    prompt  = (
        "Use the context below to answer the question:\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\nAnswer:"
    )
    st.session_state.chat_history.append({"role": "user",    "content": prompt})

    # 9) Call OpenRouter with requests so we can inspect raw response
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=st.session_state.chat_history,
        temperature=0.3
    )
    answer = response.choices[0].message.content

    # 11) Update chat history
    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    return answer

# ─── Interaction ───────────────────────────────────────────────────────────────
# 6) UI input
# show the text input always, but disable until we have chunks
parsed = uploaded and raw_text.strip() != ""

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask a question about the PDF", disabled=not parsed)
    submit = st.form_submit_button("📤 Send", use_container_width=True)

if submit and user_input:
        with st.spinner("Thinking..."):
            answer = generate_answer(user_input)
            # Inject CSS for chat bubbles
            
            # Style chat with custom CSS
            st.markdown("""
            <style>
                .user-msg {
                    background: linear-gradient(to right, #ffe259, #ffa751);  /* Yellow-orange gradient */
                    color: #000;
                    padding: 12px 16px;
                    border-radius: 12px;
                    margin: 12px 0;
                    font-weight: 500;
                }
            
        """, unsafe_allow_html=True)

        # Show chat messages with left-right separation
        st.markdown(f'User: <div class="user-msg">{user_input}</div>', unsafe_allow_html=True)
        st.markdown(f'Bot: <div class="bot-msg">{answer}</div>', unsafe_allow_html=True)