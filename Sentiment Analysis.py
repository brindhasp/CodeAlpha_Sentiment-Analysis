import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv("quotes_data.csv")

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Quote"].apply(get_sentiment)

sentiment_count = df["Sentiment"].value_counts()

plt.figure()
sentiment_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sentiment Distribution of Quotes")
plt.ylabel("")
plt.show()

print(df.head())