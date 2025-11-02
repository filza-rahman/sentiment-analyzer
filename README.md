# sentiment-analyzer
An natural language processing based sentiment analysis tool that classifies user text as Positive, Negative, or Neutral. Helpful in assessing social media comments or posts!

---

## Features
- Analyze any sentence or short paragraph for sentiment.
- Returns both:
  - **Polarity**: how positive or negative the text is (-1 to +1)
  - **Subjectivity**: how opinionated vs factual the text is (0 to 1)
- Console-based interactive input (type sentences and see instant results).
- Optional: Can be extended to analyze multiple reviews from CSV or run as a web app using Streamlit.

---

## How It Works !!
TextBlob uses a **predefined sentiment lexicon** to evaluate each word in your text:

- **Polarity**: ranges from -1 (very negative) to +1 (very positive)  
- **Subjectivity**: ranges from 0 (objective/factual) to 1 (opinionated/subjective)  

Example:
- `"I love this project!"` → Positive (Polarity: 0.8, Subjectivity: 0.75)  
- `"I hate exams."` → Negative (Polarity: -0.85, Subjectivity: 0.9)  
- `"It’s okay, I guess."` → Neutral (Polarity: 0.0, Subjectivity: 0.5)  

---

## How to Run
1. Make sure you have **Python 3.x** installed.
2. Clone or download this repository.
3. Open a terminal or command prompt in the project folder.
4. Install the required library:
```bash
pip install -r requirements.txt
Run the program:

bash

python sentiment_analyzer.py
---
Type a sentence and see the sentiment and subjectivity output!
---

Type "exit" to quit the program.
