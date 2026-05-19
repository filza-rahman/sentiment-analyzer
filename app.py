import streamlit as st
from textblob import TextBlob
import nltk

try:
    nltk.data.find('corpora/movie_reviews')
except LookupError:
    nltk.download('punctuation')
    nltk.download('movie_reviews')

import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", page_icon="🧠", layout="centered")

st.title("🧠 Simple Sentiment Analyzer")
st.write("Type a sentence below to analyze its emotional tone and subjectivity.")

user_text = st.text_area("Enter a sentence:", placeholder="Type something here...")

if st.button("Analyze Sentiment", type="primary"):
    if user_text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Analyzing..."):
            # This is your exact TextBlob logic running in the background
            blob = TextBlob(user_text)
            sentiment_score = blob.sentiment.polarity        # -1 to 1
            subjectivity_score = blob.sentiment.subjectivity  # 0 to 1

            # Determine the sentiment category
            if sentiment_score > 0:
                sentiment = "Positive"
                emoji = "😊"
            elif sentiment_score < 0:
                sentiment = "Negative"
                emoji = "😢"
            else:
                sentiment = "Neutral"
                emoji = "😐"

            # Display Results Visually on the Web Page
            st.write("---")
            st.subheader("Analysis Results:")
            
            # Using Metric blocks for a clean, professional look
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Sentiment Category", value=f"{sentiment} {emoji}")
            with col2:
                st.metric(label="Polarity Score (-1 to 1)", value=f"{sentiment_score:.2f}")
                
            st.info(f"**Subjectivity Score:** {subjectivity_score:.2f} (0 is completely factual/objective, 1 is opinion-based/subjective)")