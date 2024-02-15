import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code  200)
    if response.status_code ==  200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Save the parsed HTML to a file
        with open('./output.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print("The content has been saved to output.html")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage:
scrape_website("https://www.cnet.com/home/internet/features/the-secret-life-of-the-500-cables-that-run-the-internet/")