import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("stopwords")
nltk.download("punkt")

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    stop_words = set(stopwords.words("english"))
    
    df["cleaned_title"] = df["title"].apply(lambda x: " ".join(
        [word.lower() for word in word_tokenize(x) if word.isalnum() and word.lower() not in stop_words]
    ))
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
