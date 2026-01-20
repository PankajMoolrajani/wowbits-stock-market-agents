import os
import requests
from datetime import datetime, timedelta

def get_stock_news(symbol: str) -> list:
    """
    Get latest news articles for a given stock ticker using FMP API.
    
    Args:
        symbol (str): Stock ticker symbol
        
    Returns:
        list: List of news articles with title, description, date, etc.
    """

    print (f"Getting news for {symbol}")
    base_url = "https://financialmodelingprep.com/api/v3/stock_news"
    
    params = {
        "tickers": symbol,
        "limit": 10,
        "apikey": os.environ.get("FMP_API_KEY")
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        # Format the response data
        formatted_news = []
        for article in news_data:
            formatted_article = {
                "title": article.get("title"),
                "text": article.get("text"),
                "published_date": article.get("publishedDate"),
                "source": article.get("site"),
                "url": article.get("url"),
                "image_url": article.get("image")
            }
            formatted_news.append(formatted_article)
            
        return formatted_news
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching news data: {str(e)}")
    except ValueError as e:
        raise Exception(f"Error parsing news data: {str(e)}")


if __name__ == "__main__":
    print (get_stock_news("AAPL"))