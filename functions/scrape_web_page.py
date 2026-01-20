import os
from firecrawl import Firecrawl

def scrape_webpage(url: str):
    """
    Scrapes a webpage and returns its content in whatever format Firecrawl provides.
    
    Args:
        url (str): The URL to scrape (must include http:// or https://)
        
    Returns:
        dict | str: The scraped content (JSON/dict if multiple formats are available, or string if only one format).
    """
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    firecrawl = Firecrawl(api_key=api_key)
    result = firecrawl.scrape(url=url)
    return result
