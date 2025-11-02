# sentiment-analyzer
An NLP-based sentiment analysis tool that classifies user text as Positive, Negative, or Neutral. Helpful in assessing social media comments or posts!


## Features
- Analyze any sentence or short paragraph for sentiment.
- Gives you both **polarity** (how positive or negative) and **subjectivity** (how opinionated) of text.
- Console-based interactive input (type sentences and see instant results).

## How It Works
TextBlob uses a **predefined sentiment lexicon** to evaluate each word in your text:

- **Polarity**: ranges from -1 (very negative) to +1 (very positive)  
- **Subjectivity**: ranges from 0 (objective) to 1 (subjective/opinionated)  

Example:
- `"I love this project"` → Positive (Polarity: 0.8)  
- `"I hate exams"` → Negative (Polarity: -0.9)  
- `"I guess it's okay."` → Neutral (Polarity: 0.0)  

---

## How to Run It
1. Make sure you have **Python 3.x** installed.
2. Clone or download this repository.
3. Open a terminal or command prompt in the project folder.
4. Install the required library:
```bash
-pip install textblob

## Then run the program:
python sentiment_analyzer.py


## Type a sentence and see the sentiment output !!

## Type "exit" to quit the program.
