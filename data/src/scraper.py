import praw
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def reddit_scraper(subreddit_name, limit=100, output_file="data/raw_data.csv"):
    """
    Scrapes posts from a subreddit and saves the data to a CSV file.

    Parameters:
    - subreddit_name (str): The name of the subreddit to scrape.
    - limit (int): The number of posts to scrape. Default is 100.
    - output_file (str): Path to the output CSV file. Default is 'data/raw_data.csv'.
    
    Returns:
    - pd.DataFrame: DataFrame containing the scraped data.
    """
    # Get Reddit API credentials from environment variables
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")

    # Check if credentials are loaded
    if not client_id or not client_secret or not user_agent:
        print("Error: Missing Reddit API credentials in .env file.")
        return None

    # Initialize Reddit API connection
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    try:
        # Scrape posts from the specified subreddit
        print(f"Scraping {limit} posts from the '{subreddit_name}' subreddit...")
        subreddit = reddit.subreddit(subreddit_name)
        posts = []

        # Iterate through the posts and collect relevant data
        for post in subreddit.new(limit=limit):
            posts.append({
                "title": post.title,
                "created_utc": datetime.utcfromtimestamp(post.created_utc),
                "score": post.score,
                "num_comments": post.num_comments,
                "url": post.url  # Add post URL for reference
            })

        # Convert the posts list into a DataFrame
        df = pd.DataFrame(posts)

        # Save the data to a CSV file
        df.to_csv(output_file, index=False)
        print(f"Data scraped and saved to {output_file}")
        
        return df

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    subreddit_name = "stocks"  # Specify the subreddit
    reddit_scraper(subreddit_name, limit=100)  # Scrape 100 posts from the "stocks" subreddit
