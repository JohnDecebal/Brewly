import requests
from bs4 import BeautifulSoup

def scrape_coffee_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Implement scraping logic here
    return {'title': 'Sample Article', 'content': 'Sample content', 'source': url}