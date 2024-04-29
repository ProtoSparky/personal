from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize(text, language="english", sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])


def summarize_ai(text, context, sentences_count, ai_model, ai_api):
    #summarization using AI
    import datetime
    from ollama import Client
    current_datetime = datetime.datetime.now()
    system_promt = """You are an AI summarization tool. 
    Your job is to summarize text the same way a human would do it, using context to look for relevant information that answers the user's question. 
    You will stick to the maximum summary length of """  + str(sentences_count) + """ sentence(s), 
    and yet you will bring forward relevant information without compromising on your summary quality. 
    You will NEVER add information that was not presented in the first place.
    You will ONLY reply with the summary of the text
    The current system time is
    """ + current_datetime.strftime("%Y-%m-%d %H:%M") + " as YYYY-MM-DD HH:MM:SS."
    msg = []
    sys_msg = {"role": "system", "content": system_promt}
    user_msg ={"role": "user", "content": "Id like you to answer '" + context + "' With this text '" + text + "'"}
    msg.append(sys_msg)
    msg.append(user_msg)
    response = Client(ai_api).chat(model=ai_model, messages=msg)
    clean_response = response["message"]["content"]
    return clean_response




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

import read_website as rd
context = "What's todays weather?"
page = rd.read_website("https://www.yr.no/nb/v%C3%A6rvarsel/daglig-tabell/1-72837/Norge/Oslo/Oslo/Oslo")

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


# Parse the input text
parser = PlaintextParser.from_string(page, Tokenizer("English"))

# Create an LSA summarizer
summarizer = LsaSummarizer()

# Generate the summary
summary = summarizer(parser.document, sentences_count=15) # Adjust the number of sentences in the summary
for sentence in summary:
    print(sentence)