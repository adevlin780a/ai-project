# 🧠 Mini Sentiment Analyzer

A simple Streamlit app that analyzes text sentiment and subjectivity **offline** using the lightweight `TextBlob` library.

## ✨ Features
- Detects **positive**, **negative**, or **neutral** sentiment.
- Calculates **subjectivity** (0 = objective, 1 = subjective).
- Runs entirely **offline** — no tokens, no API calls.

## 🚀 Quick Start
1. Clone or unzip the project folder.
2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate     # macOS / Linux
   .\.venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```
5. Visit http://localhost:8501 in your browser.

## 🧩 Tech Stack
- **Streamlit** for the web interface.
- **TextBlob** for local NLP (sentiment + subjectivity).

## 💾 Storage
- Project files: < 5 MB
- Dependencies: ~20 MB
- **Total estimated size:** ~25 MB

## 📁 Files
- `app.py` — main app
- `requirements.txt` — dependencies
- `README.md` — documentation
