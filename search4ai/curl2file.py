import requests
from bs4 import BeautifulSoup

############################################################################################
############################################################################################
############################################################################################
#this script copies all data from a website

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
############################################################################################
############################################################################################
############################################################################################

#this script copies everything, and tries to filter away css and js

def scrape_and_filter_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code  200)
    if response.status_code ==  200:
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
        
        # Save the parsed HTML to a file
        with open('./output.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print("The content has been saved to output.html")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
############################################################################################
############################################################################################
############################################################################################
#this function scrapes and converts the text in a website to a txt file

def read_website(url):
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
        
        # Save the extracted text to a file
        with open('./extracted_text.txt', 'w', encoding='utf-8') as f:
            for text in text_nodes:
                f.write(text + '\n')
        
        print("The content has been saved to extracted_text.txt")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage:
scrape_website("http://protosparky.uk")