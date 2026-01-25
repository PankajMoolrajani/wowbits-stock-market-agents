import os
import requests
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()



def get_stock_twitter_feed(ticker: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """
    Get Twitter feed for a given stock ticker.
    
    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'TSLA')
        max_results: Maximum number of tweets to return (default: 10)
    
    Returns:
        List of dictionaries containing tweet information
    """
    # Note: This requires Twitter API v2 credentials
    # Set these environment variables: TWITTER_BEARER_TOKEN
    
    bearer_token = os.environ.get('X_BEARER_TOKEN')
    
    if not bearer_token:
        return {
            'error': 'Twitter API credentials not configured',
            'message': 'Please set TWITTER_BEARER_TOKEN environment variable'
        }
    
    # Search query for the stock ticker with cashtag
    query = f"${ticker} OR #{ticker}"
    
    # Twitter API v2 endpoint
    url = "https://api.twitter.com/2/tweets/search/recent"
    
    # Parameters for the request
    params = {
        'query': query,
        'max_results': max(10, min(max_results, 100)),  # API requires 10-100
        'tweet.fields': 'created_at,author_id,public_metrics,text',
        'expansions': 'author_id',
        'user.fields': 'username,name,verified_type'
    }
    
    # Headers with bearer token
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Parse and format the response
        tweets = []
        users = {}
        
        # Create a user lookup dictionary
        if 'includes' in data and 'users' in data['includes']:
            for user in data['includes']['users']:
                users[user['id']] = user
        
        # Format tweets
        if 'data' in data:
            for tweet in data['data']:
                author = users.get(tweet.get('author_id'), {})
                
                tweets.append({
                    'id': tweet.get('id'),
                    'text': tweet.get('text'),
                    'created_at': tweet.get('created_at'),
                    'author': {
                        'username': author.get('username'),
                        'name': author.get('name'),
                        'verified_type': author.get('verified_type')
                    },
                    'metrics': tweet.get('public_metrics', {}),
                    'url': f"https://twitter.com/{author.get('username', 'i')}/status/{tweet.get('id')}"
                })
        
        return {
            'ticker': ticker,
            'tweet_count': len(tweets),
            'tweets': tweets
        }
    
    except requests.exceptions.RequestException as e:
        return {
            'error': 'Failed to fetch Twitter feed',
            'message': str(e),
            'ticker': ticker
        }


if __name__ == "__main__":
    print (get_stock_twitter_feed("AAPL"))