import os
import requests

def get_stock_fundamentals(symbol: str) -> dict:
    """
    Get fundamental financial data for a given stock symbol using Financial Modeling Prep API.
    
    Args:
        symbol (str): The stock symbol to look up (e.g. 'AAPL', 'GOOGL')
        
    Returns:
        dict: Dictionary containing fundamental data including:
            - Market Cap
            - P/E Ratio
            - EPS
            - Revenue
            - Profit Margin
            - And other key metrics
        
    Raises:
        Exception: If there is an error fetching the fundamentals data
    """
    print (f"Getting fundamentals for symbol: {symbol}")
    # FMP API endpoint and parameters
    url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}"
    params = {
        "apikey": os.environ.get("FMP_API_KEY")
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print (f"Fundamental data: {data}")
        if not data:
            raise Exception(f"No fundamental data found for symbol: {symbol}")

        # Extract relevant fundamental metrics
        fundamentals = {
            "marketCap": data[0].get("mktCap"),
            "price": data[0].get("price"),
            "beta": data[0].get("beta"),
            "volAvg": data[0].get("volAvg"),
            "lastDiv": data[0].get("lastDiv"),
            "range": data[0].get("range"),
            "changes": data[0].get("changes"),
            "companyName": data[0].get("companyName"),
            "currency": data[0].get("currency"),
            "sector": data[0].get("sector"),
            "industry": data[0].get("industry"),
            "website": data[0].get("website"),
            "description": data[0].get("description"),
            "ceo": data[0].get("ceo"),
            "country": data[0].get("country")
        }
        
        return fundamentals

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching stock fundamentals: {str(e)}")
    except (KeyError, ValueError, IndexError) as e:
        raise Exception(f"Error parsing fundamentals data: {str(e)}")
