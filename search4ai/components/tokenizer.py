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








def chunkenizer(textinput):
    import spacy
    #english models available en_core_web_sm, en_core_web_trf
    #command to download models python -m spacy download <model name>
    nlp = spacy.load("en_core_web_trf")
    # Split the text into chunks using spaCy's sentence splitter
    doc = nlp(textinput)
    chunks = [sent.text for sent in doc.sents]
    return chunks



def LinkClassifier(Link):
    from ollama import Client
    LinkClassifierSettings = {"api":"http://localhost:11434/api", "model":"llama3"}
    SystemPrompt = "Your goal is to classify a link that the user sends you as something like 'news' for a news website, 'weather' for a weather website, etc. Your reply MUST ONLY contain the category of classification"
    msg = []
    sys_msg = {"role": "system", "content": SystemPrompt}
    msg.append(sys_msg)
    usr_msg = {"role":"user", "content":"Classify this link '" + Link + "'"}
    msg.append(usr_msg)
    response = Client(LinkClassifierSettings["api"]).chat(model=LinkClassifierSettings["model"], messages=msg)
    response_clean = response["message"]["content"]
    return response_clean


def SumByCategory(Category, Text):
    from ollama import Client
    LinkClassifierSettings = {"api":"http://localhost:11434/api", "model":"llama3"}
    SystemPrompt = """
    Your task is to refine the provided content based on the user-provided context, without altering the original meaning or structure of the text. The refined text should strictly adhere to the user-provided context. For instance, if the context is 'weather', your job is to extract and retain only the weather-related information from the user-submitted text, excluding irrelevant details such as cookie policies, about sections, etc.

    For other categories, apply the same principle of retaining only the relevant information based on the context. The refined text should not be a mere list or bullet points of the contextual information. Instead, it should maintain the coherence and structure of the original text, while effectively trimming away any information that does not fit within the provided context.
    """
    msg = []
    sys_msg = {"role": "system", "content": SystemPrompt}
    msg.append(sys_msg)
    usr_msg = {"role":"user", "content":"The category for this text is '" + Category + "'. Trim this text '" + Text + "'"}
    msg.append(usr_msg)
    response = Client(LinkClassifierSettings["api"]).chat(model=LinkClassifierSettings["model"], messages=msg)
    response_clean = response["message"]["content"]
    return response_clean


url = "https://www.vg.no/nyheter/innenriks/i/bmK7kg/elever-dropper-russetiden-ola-svenneby-stoetter-dem?utm_source=vgfront&utm_content=hovedlopet_row1_pos1&utm_term=dre-vg-bmK7kg-1714421558%3Adre-662fff36c1bc995ba0b5f544&utm_medium=dre-662fff36c1bc995ba0b5f544"
site = scrape_and_filter_website(url)
category = LinkClassifier(url)
print(SumByCategory(category, site))



from transformers import GPT2Tokenizer

def estimate_tokens(input_text):
    # Load pre-trained GPT-2 tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Tokenize the input text and count the number of tokens
    tokens = tokenizer.encode(input_text)
    num_tokens = len(tokens)
    return num_tokens

#print(site)

