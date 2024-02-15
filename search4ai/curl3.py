import requests
from bs4 import BeautifulSoup
import random

def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT  6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Windows NT  6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X  10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS  11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Mozilla/5.0 (Windows NT  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    ]
    return random.choice(user_agents)
def get_html_without_js_and_css(url):
    # Fetch the webpage content
    headers = {
        'User-Agent': get_random_user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '0',  # Do Not Track header
        'Connection': 'keep-alive'
    }
    response = requests.get(url, headers=headers, stream=False)
    
    # Check if the request was successful
    if response.status_code ==   200:
        # Convert the content to a string
        html_content = response.content.decode('utf-8')
        
        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script tags, noscript tags, style tags, and svg tags
        for tag in soup(['script', 'noscript', 'style', 'svg']):
            tag.decompose()
        
        # Remove inline styles
        for tag in soup.find_all(True):
            if 'style' in tag.attrs:
                del tag['style']
        
        # Remove class and id attributes
        for tag in soup.find_all(True):
            if 'class' in tag.attrs:
                del tag['class']
            if 'id' in tag.attrs:
                del tag['id']
        
        # Return the cleaned HTML content
        return str(soup)
    else:
        return None

url = 'https://www.cnet.com/home/internet/features/the-secret-life-of-the-500-cables-that-run-the-internet/'
html_content = get_html_without_js_and_css(url)
print(html_content)