import streamlit as st
from textblob import TextBlob

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Technical Writing Objectivity Analyzer", layout="centered")

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
<style>
/* Main background */
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
    color: #000000;
}

/* Header bar */
header[data-testid="stHeader"] {
    background-color: #f46b36;
    color: #ffffff;
}

/* Header text */
header[data-testid="stHeader"] * {
    color: #ffffff !important;
}

/* Buttons */
div.stButton > button:first-child {
    background-color: #f46b36;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    padding: 0.6em 1.2em;
    border: none;
}
div.stButton > button:first-child:hover {
    background-color: #d85e2f;
    color: white;
}

/* Metric styling */
[data-testid="stMetricValue"] {
    color: #000000 !important;
}
[data-testid="stMetricLabel"] {
    color: #000000 !important;
}

/* Text area customization */
textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #d3d3d3 !important;
    border-radius: 6px !important;
    padding: 0.5em !important;
}

/* Fix label ("Paste your writing sample below") */
div[data-testid="stTextArea"] label p {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* Remove shadow on focus */
textarea:focus {
    outline: none !important;
    box-shadow: 0 0 4px #f46b36 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- APP TITLE ----------------
st.title("Technical Writing Objectivity Analyzer")
st.markdown(
    "Check how **objective or subjective** your writing sounds. "
    "This tool helps you refine your tone to be clear, factual, and professional — "
    "perfect for documentation, reports, or any technical writing."
)

# ---------------- TEXT INPUT ----------------
text = st.text_area("Paste your writing sample below:", height=200, placeholder="Type or paste your text here...")

# ---------------- ANALYSIS ----------------
if st.button("Analyze Objectivity"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        blob = TextBlob(text)
        subjectivity = blob.sentiment.subjectivity
        objectivity = 1 - subjectivity

        # Feedback message
        if objectivity > 0.75:
            feedback = "✅ Excellent! Your writing is clear, factual, and objective."
        elif objectivity > 0.5:
            feedback = "🟠 Fairly objective — consider reducing opinionated language or emotional phrasing."
        else:
            feedback = "⚠️ This reads as subjective or opinionated. Aim for more neutral, fact-based wording."

        # Display results
        st.subheader("Results")
        st.metric("Objectivity Score", f"{objectivity:.2f}")
        st.metric("Subjectivity Score", f"{subjectivity:.2f}")
        st.markdown(f"**Feedback:** {feedback}")

        # Add explanation of how AI gauges objectivity
        st.markdown("""
        ---
        **How This Works:**  
        The analyzer uses the open-source AI library **TextBlob**, which applies a trained natural language model to evaluate how factual or opinion-based your text is.  
        - It looks for *subjective patterns* such as emotional adjectives, personal opinions, and uncertain phrasing.  
        - Each word and phrase contributes to an overall *subjectivity score*, where higher values mean more opinionated writing.  
        - The *objectivity score* is then calculated as the inverse — showing how clear, evidence-based, and factual your writing is.  

        This approach is lightweight but effective for understanding tone, making it a useful tool for writers who want to keep their documentation or reports balanced and professional.
        """)

# ---------------- WRITING TIPS (Always Visible) ----------------
st.divider()
st.markdown("""
### Writing Tips for Better Objectivity
Here are some proven strategies for making your writing more clear, factual, and objective:

1. **Avoid personal phrases** — Skip "I think," "I feel," or "in my opinion." These make your text sound subjective.  
   ✅ *Better:* Replace with direct, factual statements like “Results indicate that…”  

2. **Replace emotional adjectives** — Words like *great*, *terrible*, or *amazing* express emotion rather than fact.  
   ✅ *Better:* Use measurable terms such as *effective*, *inefficient*, or *high-performing*.  

3. **Use active voice and clear verbs** — Say *“The team completed the update”* instead of *“The update was completed.”*  
   Active voice keeps writing strong and readable.  

4. **Support claims with data or evidence** — Replace opinions with proof.  
   ✅ *Better:* “Testing reduced errors by 15%,” instead of “The tool works.”  

5. **Be consistent and precise** — Avoid vague terms like “some,” “many,” or “recently.”  
   ✅ *Better:* “42% of users reported the issue within two days.”  

By applying these principles, you can make your writing more credible, professional, and easy to trust.
""")

# ---------------- ABOUT SECTION ----------------
st.divider()
st.markdown("""
### About
This project uses **TextBlob**, an open-source natural language processing (NLP) library built on top of NLTK.  
TextBlob analyzes your text using a lexicon-based AI model which is a dictionary of words rated for their emotional and subjective tone. 
             
By averaging those values and adjusting for negations and modifiers, the system determines how objective or opinionated a passage sounds.  
  
""")
