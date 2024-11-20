from src.scraper import reddit_scraper
from src.preprocessing import clean_data
from src.sentiment import add_sentiment
from src.model import train_model

def main():
    # Scraping
    print("Scraping data from Reddit...")
    reddit_scraper("stocks", limit=200)
    
    # Preprocessing
    print("Cleaning data...")
    clean_data("data/raw_data.csv", "data/cleaned_data.csv")
    
    # Sentiment Analysis
    print("Performing sentiment analysis...")
    add_sentiment("data/cleaned_data.csv", "data/enhanced_data.csv")
    
    # Model Training
    print("Training the model...")
    train_model("data/enhanced_data.csv")

if __name__ == "__main__":
    main()
