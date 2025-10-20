# Technical Writing Objectivity Analyzer

The **Technical Writing Objectivity Analyzer** is a lightweight AI web app that helps writers evaluate how **objective or subjective** their text sounds. It’s designed for technical writers, editors, students, and professionals who want to make their writing clearer, more factual, and less opinion-based.

Built with **Python**, **Streamlit**, and **TextBlob**, this tool runs entirely on your local machine. No internet connection or API key required. It provides instant feedback and practical writing tips to improve clarity and tone.

---

## How It Works

When you paste your writing and click “Analyze Objectivity”, the app uses **TextBlob**, an open-source natural language processing (NLP) library, to examine your text.

It calculates two key metrics:
- **Subjectivity Score:** How much of your text expresses personal opinion or emotion.
- **Objectivity Score:** The opposite of subjectivity or how clear, factual, and unbiased your writing is.

### How the AI Evaluates Objectivity
TextBlob uses a **lexicon-based AI model**, which means it has a dictionary of words labeled for how emotional or factual they are.  
When you analyze text:
1. It scans each word and phrase to detect subjectivity or emotion.  
2. It averages those values to calculate a *subjectivity score*.  
3. It then inverts that value to produce an *objectivity score*.  

This lightweight method doesn’t rely on external servers or complex APIs, everything happens locally on your computer.

---

## Features

- Simple, modern web interface built with **Streamlit**
- Instant AI-powered objectivity and subjectivity analysis
- Practical writing tips for improving tone and clarity
- Runs completely offline after installation
- Clean and accessible color scheme (white, orange, and black)

---

## Writing Tips for Better Objectivity

Here are some proven strategies the app recommends for improving writing quality:

1. **Avoid personal phrases** — Skip “I think,” “I feel,” or “in my opinion.”  
   *Better:* Replace with direct statements like “Results indicate that…”  

2. **Replace emotional adjectives** — Avoid “great,” “terrible,” or “amazing.”  
   *Better:* Use measurable terms like “effective,” “inefficient,” or “high-performing.”  

3. **Use active voice** — “The team completed the update” is clearer than “The update was completed.”  

4. **Support claims with data or evidence** — Replace opinions with proof.  
   *Better:* “Testing reduced errors by 15%.”  

5. **Be specific** — Avoid vague words like “some,” “many,” or “recently.”  
   *Better:* “42% of users reported the issue within two days.”  

---

## Getting Started (For Beginners)

Follow these simple steps to download and run the app on your own computer.

### 1. Install Python
You’ll need **Python 3.9 or higher** installed.  
- Download it from: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
- When installing, **check the box that says “Add Python to PATH”** before clicking *Install Now*.

### 2. Download This Project
You can get the project files in one of two ways:
- Click the green **“Code”** button on this page and choose **“Download ZIP”**.  
  Then unzip the file anywhere on your computer.  
- OR, if you use GitHub Desktop, click **“Open with GitHub Desktop”** to clone the repository.

### 3. Open a Terminal or Command Prompt
On your computer:
- **Windows:** Open *Command Prompt* or *PowerShell*  
- **Mac/Linux:** Open *Terminal*

Use the `cd` command to move into the folder where you unzipped or cloned the project.  
For example:
```bash
cd Downloads/technical-writing-objectivity-analyzer
```

### 4. Install the Required Packages
In the terminal, run:

```pip install -r requirements.txt```


If you don’t see a `requirements.txt` file, you can install the two needed libraries manually:

```pip install streamlit textblob```

### 5. Run the App

After installation, start the app by running:

```streamlit run app.py```


This will open the app in your web browser automatically.
If not, look for a link like:

```Local URL: http://localhost:8501```


Click it or copy it into your browser.


## Troubleshooting (Linux Users)

If you see an error like:

`error: externally-managed-environment` or

`bash: .venv/bin/pip: cannot execute: required file not found`

follow these steps to fix it:

1. Install Full Python and venv Support
Exit any existing virtual environment first:

```deactivate```

Then install missing packages:

```sudo apt update```
```sudo apt install python3-full python3-venv python3-pip -y```

2. Remove Any Broken Virtual Environment

```rm -rf .venv```

3. Create a New Virtual Environment

```python3 -m venv .venv```
```source .venv/bin/activate```

You should now see `(.venv)` in your terminal prompt.

4. Reinstall Dependencies

```pip install --upgrade pip```
```pip install -r requirements.txt```

5. Run the App Again

```streamlit run app.py```

Your app should now start correctly and open in your browser.



