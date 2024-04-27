import requests
from bs4 import BeautifulSoup
def read_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code   200)
        if response.status_code ==   200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
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
            
            # Extract text nodes containing more than one word
            text_nodes = [node for node in soup.stripped_strings if len(node.split()) >  1]
            total_str = ""
            for line in text_nodes:
                total_str = total_str + line + "\n"
            return total_str
        else:
            print(f"Failed to retrieve the webpage. Status code: else {response.status_code}")
            return f"Failed to retrieve the webpage. Status code: except {response.status_code} Ask user for guidance"
    except:
            print(f"Failed to retrieve the webpage. Status code: except {response.status_code}")
            return f"Failed to retrieve the webpage. Status code: except {response.status_code} Ask user for guidance"
