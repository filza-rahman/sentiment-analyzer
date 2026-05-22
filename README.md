# sentiment-analyzer

An NLP-based sentiment analysis tool that classifies user text as **Positive**, **Negative**, or **Neutral** — originally built as a terminal script, now deployed as an interactive web app.

🔗 **[Live demo](https://filzas-sentiment-analyzer.streamlit.app/)**

---

## What it does

Paste or type any sentence and get back:

- **Sentiment**: Positive, Negative, or Neutral
- **Polarity**: how positive or negative the text is (−1 to +1)
- **Subjectivity**: how opinionated vs. factual (0 to 1)

**Examples:**
| Input | Sentiment | Polarity | Subjectivity |
|---|---|---|---|
| `"I love this project!"` | Positive | 0.80 | 0.75 |
| `"I hate exams."` | Negative | −0.85 | 0.90 |
| `"It's okay, I guess."` | Neutral | 0.00 | 0.50 |

---

## How it works

TextBlob evaluates each word against a predefined sentiment lexicon to score **polarity** and **subjectivity**, then maps the polarity score to a label:

- `> 0.15` → Positive
- `< -0.15` → Negative
- In between → Neutral

---

## Files

| File | Description |
|---|---|
| `sentiment_analyzer.py` | Original terminal-based script |
| `app.py` | Streamlit web app version |
| `requirements.txt` | Dependencies |

---

## Run locally

```bash
git clone https://github.com/filza-rahman/sentiment-analyzer
cd sentiment-analyzer
pip install -r requirements.txt

# Terminal version
python sentiment_analyzer.py

# Web app version
streamlit run app.py
```

---

## Built with

- [Python 3](https://www.python.org/)
- [TextBlob](https://textblob.readthedocs.io/)
- [Streamlit](https://streamlit.io/)
