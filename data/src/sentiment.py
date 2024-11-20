from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import nltk

nltk.download("vader_lexicon")

def add_sentiment(input_file, output_file):
    df = pd.read_csv(input_file)
    sia = SentimentIntensityAnalyzer()
    
    df["sentiment"] = df["cleaned_title"].apply(lambda x: sia.polarity_scores(x)["compound"])
    df.to_csv(output_file, index=False)
    print(f"Sentiment scores added and saved to {output_file}")
