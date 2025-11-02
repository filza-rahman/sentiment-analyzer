from textblob import TextBlob

print(" Simple Sentiment Analyzer ")
print("Type 'exit' to quit.\n")

while True:
    text = input("Enter a sentence: ")
    if text.lower() == 'exit':
        print("Goodbye! ")
        break

    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Range: -1 (negative) to +1 (positive)

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Sentiment: {sentiment} (Score: {sentiment_score:.2f})\n")

