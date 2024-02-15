import requests
from bs4 import BeautifulSoup
import re

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
read_website("https://ndla.no/subject:846a7552-ea6c-4174-89a4-85d6ba48c96e/topic:c4519d4e-c0d5-467c-bba9-6cff3e7c64cb/topic:257b2ce7-d151-4c80-87c3-ae2f4814d52f/resource:470f02b1-4098-42f8-8715-cd639d8b216e")