import requests
from bs4 import BeautifulSoup
import html2text

def scrape_and_filter_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
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

        # Convert the cleaned HTML to Markdown
        h = html2text.HTML2Text()
        h.ignore_links = False
        markdown_text = h.handle(str(soup))
        
        return markdown_text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



page = scrape_and_filter_website("https://www.yr.no/nb/v%C3%A6rvarsel/daglig-tabell/1-72837/Norge/Oslo/Oslo/Oslo")



import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_trf")
# Placeholder function for processing each chunk
def process_chunk(chunk):
    # Your model's processing logic here
    return chunk # Return the processed chunk



# Split the text into chunks using spaCy's sentence splitter
doc = nlp(page)
chunks = [sent.text for sent in doc.sents]

# Process each chunk with your AI model
# This is a placeholder for your model's processing logic
processed_chunks = [process_chunk(chunk) for chunk in chunks]
print(processed_chunks)
# Combine the processed chunks
combined_result = " ".join(processed_chunks)
