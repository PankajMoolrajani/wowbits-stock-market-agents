import os
import requests

def get_stock_price(symbol: str) -> float:
    """
    Get the current stock price for a given symbol using Financial Modeling Prep API.
    
    Args:
        symbol (str): The stock symbol to look up (e.g. 'AAPL', 'GOOGL')
        
    Returns:
        float: The current stock price
        
    Raises:
        Exception: If there is an error fetching the stock price
    """
    # FMP API endpoint and parameters
    url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}"
    params = {
        "apikey": os.environ.get("FMP_API_KEY")
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            raise Exception(f"No price data found for symbol: {symbol}")
            
        # Extract the current price from response
        price = float(data[0]["price"])
        return price
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching stock price: {str(e)}")
    except (KeyError, ValueError, IndexError) as e:
        raise Exception(f"Error parsing stock price data: {str(e)}")
