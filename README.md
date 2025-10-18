# Technical Writing Objectivity Analyzer

The **Technical Writing Objectivity Analyzer** is a lightweight AI-powered web app that helps writers evaluate how **objective** or **subjective** their writing sounds.  
It’s designed especially for **technical writers, editors, and students** who want to produce clear, factual, and unbiased content for documentation or professional communication.

This project runs entirely **locally** using the open-source **TextBlob** library — no tokens, no API keys, and no internet connection required.

---

## How It Works

When you paste a piece of writing into the app and click **Analyze Objectivity**, the tool uses **TextBlob**, a natural language processing (NLP) library built on top of NLTK, to measure two main qualities:

- **Subjectivity Score** – Indicates how opinionated or emotional the writing is.  
  Ranges from 0.0 (fully objective) to 1.0 (highly subjective).
- **Objectivity Score** – The inverse of subjectivity, showing how factual or neutral the text is.  
  Higher scores indicate writing that is more evidence-based and less emotional.

TextBlob performs this analysis using a **lexicon-based AI model**, meaning it references a dictionary of words that have been rated for emotional and subjective tone.  
Each word contributes to the overall score, and TextBlob adjusts for negations (like “not good”) and modifiers (like “very strong”) to create a realistic measure of tone.

---

## Features

- Local AI processing — no internet or API required  
- Simple and intuitive Streamlit interface  
- Color-coded feedback with objectivity and subjectivity scores  
- Built-in writing improvement tips for better clarity and neutrality  
- Lightweight setup — only two Python libraries required

---

## Writing Tips for Better Objectivity

To make writing clearer, factual, and professional, the app provides built-in writing tips such as:

1. **Avoid personal phrases** – Skip “I think,” “I feel,” or “in my opinion.”  
   *Better:* “The data shows that…”  

2. **Replace emotional adjectives** – Instead of *great* or *terrible*, use measurable terms like *effective* or *inefficient.*  

3. **Use active voice and clear verbs** – “The team completed the update” is stronger than “The update was completed.”  

4. **Support claims with evidence** – Use data or results rather than personal opinions.  

5. **Be precise** – Avoid vague words like “some” or “many”; use quantifiable details where possible.  

These principles help writers maintain a neutral tone and strengthen credibility in documentation or analysis.

---

## Tech Stack

- **Python 3** – Core programming language  
- **Streamlit** – Web app framework for interactivity  
- **TextBlob** – Natural language processing and sentiment analysis  

---

## Installation and Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/adevlin780a/ai-project.git
   cd ai-project
