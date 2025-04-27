# 🏪 Medical Chatbot A.I+

A Flask-based medical chatbot application powered by LLMs (e.g., Llama 2).  
This project allows users to ask health-related questions and receive intelligent AI-generated responses.

---

## 📂 Project Structure

```
🖌️ app.py                # Main Flask application
📂 model_files/                # Pretrained LLM model binaries (e.g., .bin, model.txt)
📂 src/
📌 db/               # Database helpers (e.g., Pinecone index management)
📌 helper/           # Utility modules (config management, HuggingFace API helpers)
📌 model/            # Model loading and Retrieval-Augmented Generation (RAG) logic
📌 static/           # Frontend CSS styles
📌 templates/        # HTML templates (chat UI)

🖌️ requirements.txt      # Python dependencies
🖌️ README.md             # Project documentation (this file)
```
## 👅 Download the Llama 2 Model
We are using **Llama 2 7B Chat** model (compressed GGML format).

👉 You can download the model from [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

Recommended file:
```
llama-2-7b-chat.ggmlv3.q4_0.bin
```
Save the model inside the `model/` directory.

> **Note**: You can use a different GGML model version depending on your hardware.

---

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/fury-r/medical-chatbot-rag.git
   cd medical-chatbot-rag
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**

   Create a `.env` file or export variables:

   ```env
   HUGGINGFACE_API_TOKEN=your_huggingface_token
   PINECONE_API_KEY=your_pinecone_key
   PINECONE_ENV=your_pinecone_environment
   PINECONE_INDEX_NAME=your_index_name
   HUGGING_FACE_MODEL_NAME=name_or_id_of_model
   MODEL_PATH=path/to/your/.bin/file
   MODEL_TYPE=
   MODEL_TOKEN_LIMIT=
   MODEL_TEMPERATURE=
   MODEL_MEMORY= //optonal
   ```

4. **Start the app**
   ```bash
   python app.py
   ```

5. Open [http://localhost:5000](http://localhost:5000) in your browser 🎯

---

## 💅 Features

- 🏥 Medical domain-focused chatbot
- 🛼 Retrieval-Augmented Generation (RAG) supported
- 💬 Modern Chat UI (dark mode)
- 🔗 Integrated with HuggingFace Inference API (optional)
- 🔍 Pinecone Vector Search for context retrieval
- 📦 Local model serving (with `.bin` weights)

---


---

## 🛠️ Tech Stack

- **Backend:** Flask
- **Frontend:** Vanilla JavaScript + HTML/CSS
- **LLM Models:** Llama 2, HuggingFace models
- **Vector Database:** Pinecone
- **Model Serving:** Local or Remote

---

## ⚙️ Configuration

You can manage all environment variables and model paths using the `Config` class in `src/helper/config.py`.

---

## ✨ Future Improvements

- User Authentication (Login/Signup)
- Chat History Saving (DB Storage)
- Better Medical Disclaimer System
- Real-time Typing Indicators

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
